# Apache JMeter

## Apache JMeter

```xml
<!-- test-plan.jmx (simplified representation) -->
<?xml version="1.0" encoding="UTF-8"?>
<jmeterTestPlan version="1.2">
  <hashTree>
    <TestPlan testname="API Performance Test">
      <ThreadGroup testname="Users">
        <elementProp name="ThreadGroup.main_controller">
          <stringProp name="ThreadGroup.num_threads">50</stringProp>
          <stringProp name="ThreadGroup.ramp_time">60</stringProp>
          <stringProp name="ThreadGroup.duration">300</stringProp>
        </elementProp>

        <!-- HTTP Request: Get Products -->
        <HTTPSamplerProxy testname="GET /products">
          <stringProp name="HTTPSampler.domain">api.example.com</stringProp>
          <stringProp name="HTTPSampler.path">/products</stringProp>
          <stringProp name="HTTPSampler.method">GET</stringProp>
        </HTTPSamplerProxy>

        <!-- Assertions -->
        <ResponseAssertion testname="Response Code 200">
          <stringProp name="Assertion.test_field">Assertion.response_code</stringProp>
          <stringProp name="Assertion.test_type">8</stringProp>
          <stringProp name="Assertion.test_string">200</stringProp>
        </ResponseAssertion>

        <DurationAssertion testname="Response Time < 500ms">
          <stringProp name="DurationAssertion.duration">500</stringProp>
        </DurationAssertion>

        <!-- Timers -->
        <ConstantTimer testname="Think Time">
          <stringProp name="ConstantTimer.delay">2000</stringProp>
        </ConstantTimer>
      </ThreadGroup>
    </TestPlan>
  </hashTree>
</jmeterTestPlan>
```

```bash
# Run JMeter test
jmeter -n -t test-plan.jmx -l results.jtl -e -o report/

# Generate report from results
jmeter -g results.jtl -o report/
```
