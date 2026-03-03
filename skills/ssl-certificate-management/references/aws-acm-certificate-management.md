# AWS ACM Certificate Management

## AWS ACM Certificate Management

```yaml
# acm-certificates.yaml
resource "aws_acm_certificate" "main" {
  domain_name       = "myapp.com"
  validation_method = "DNS"

  subject_alternative_names = [
    "www.myapp.com",
    "api.myapp.com",
    "*.myapp.com"
  ]

  tags = {
    Name = "myapp-certificate"
  }

  lifecycle {
    create_before_destroy = true
  }
}

# Create Route53 validation records
resource "aws_route53_record" "cert_validation" {
  for_each = {
    for dvo in aws_acm_certificate.main.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = aws_route53_zone.main.zone_id
}

# Validate certificate
resource "aws_acm_certificate_validation" "main" {
  certificate_arn           = aws_acm_certificate.main.arn
  timeouts {
    create = "5m"
  }

  depends_on = [aws_route53_record.cert_validation]
}

# Use in ALB
resource "aws_lb_listener" "https" {
  load_balancer_arn = aws_lb.main.arn
  port              = "443"
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-TLS-1-2-2017-01"
  certificate_arn   = aws_acm_certificate_validation.main.certificate_arn

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.main.arn
  }
}
```
