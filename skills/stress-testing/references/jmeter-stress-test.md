# JMeter Stress Test

## JMeter Stress Test

```xml
<!-- stress-test.jmx -->
<jmeterTestPlan>
  <ThreadGroup testname="Stress Test Thread Group">
    <!-- Ultimate Thread Group for advanced load patterns -->
    <elementProp name="ThreadGroup.main_controller">
      <!-- Stage 1: Ramp up to 100 users -->
      <collectionProp name="ultimatethreadgroupdata">
        <stringProp>100</stringProp>  <!-- Users -->
        <stringProp>60</stringProp>   <!-- Ramp-up (sec) -->
        <stringProp>300</stringProp>  <!-- Duration (sec) -->
      </collectionProp>

      <!-- Stage 2: Ramp up to 500 users -->
      <collectionProp name="ultimatethreadgroupdata">
        <stringProp>500</stringProp>
        <stringProp>120</stringProp>
        <stringProp>600</stringProp>
      </collectionProp>

      <!-- Stage 3: Ramp up to 1000 users (stress) -->
      <collectionProp name="ultimatethreadgroupdata">
        <stringProp>1000</stringProp>
        <stringProp>180</stringProp>
        <stringProp>600</stringProp>
      </collectionProp>
    </elementProp>

    <HTTPSamplerProxy testname="Heavy Query">
      <stringProp name="HTTPSampler.domain">api.example.com</stringProp>
      <stringProp name="HTTPSampler.path">/api/search?q=stress</stringProp>
      <stringProp name="HTTPSampler.method">GET</stringProp>
    </HTTPSamplerProxy>

    <!-- Monitor for errors and degradation -->
    <ResponseAssertion testname="Allow 503 During Stress">
      <stringProp name="Assertion.test_field">Assertion.response_code</stringProp>
      <stringProp name="Assertion.test_type">8</stringProp>
      <stringProp>200|503</stringProp>
    </ResponseAssertion>
  </ThreadGroup>
</jmeterTestPlan>
```
