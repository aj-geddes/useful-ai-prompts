# Email Templates with Mjml

## Email Templates with Mjml

```html
<!-- templates/welcome.mjml -->
<mjml>
  <mj-body>
    <mj-container>
      <mj-section>
        <mj-column>
          <mj-image width="100px" src="https://example.com/logo.png"></mj-image>
        </mj-column>
      </mj-section>

      <mj-section background-color="#f4f4f4">
        <mj-column>
          <mj-text font-size="24px" align="center" color="#333">
            Welcome, {{ userName }}!
          </mj-text>
          <mj-text align="center" color="#666">
            Thank you for joining us. Let's get started!
          </mj-text>
        </mj-column>
      </mj-section>

      <mj-section>
        <mj-column>
          <mj-button
            href="https://example.com/dashboard"
            background-color="#007bff"
          >
            Go to Dashboard
          </mj-button>
        </mj-column>
      </mj-section>

      <mj-section>
        <mj-column>
          <mj-text font-size="12px" align="center" color="#999">
            © 2024 Example Inc. All rights reserved.
          </mj-text>
        </mj-column>
      </mj-section>
    </mj-container>
  </mj-body>
</mjml>

<!-- Python template compilation -->
# email_templates.py from mjml import mjml_to_html def
get_welcome_template(user_name): with open('templates/welcome.mjml', 'r') as f:
mjml_content = f.read() mjml_content = mjml_content.replace('{{ userName }}',
user_name) html = mjml_to_html(mjml_content) return html
```
