

# Handling API Breaking Changes 


Imagine you’re designing and maintaining an internal or public-facing **Weather API**. A basic version of the response looks like:

```
{
  "Weather": [
    { "hour": 0, "temperature": "18", "condition": "Clear" },
    { "hour": 1, "temperature": "17", "condition": "Clear" },
    ...
    { "hour": 23, "temperature": "16", "condition": "Cloudy" }
 ]
}
```

 Assumming this is the first published contract is consumed by multiple frontend apps already we need to introduced a change. please answer to these questions:
 

### 1 What Is a Breaking Change?

Provide examples of what would constitute a **breaking change** to this API response for the frontends that are using tihs endpoints. provide at least 3 example.

*A braking change is a change that modifies or removes the structure of the existing contract, which is what the client is expecting to find in the response. Given that we are dealing with a json file changes to the keys are breaking. So removing the outmost key "Weather" is one for example. Changing each key name is another breaking change (example changing from "temperature" to "temp" or even to "Temperature", changing the key "hour" to "hr", from "condition" to "cond" and so on).* 

*Another breaking change is if the api is supposed to return always a 24 element array and at somepoint a new version returns for example only data related to the morning.*

*Also in the given json clients are expecting hours in 24h format. Changing that to am/pm format can be a breaking change because in the old contract clients might rely on reading just an integer, whereas now they might apply extra transformation*.

1) removal of one or more existing keys is a breaking change: access to an element of the array changed from `result["Weather"][0]` to `result[0]`

```
[
  { "hour": 0, "temperature": "18", "condition": "Clear" },
  { "hour": 1, "temperature": "17", "condition": "Clear" },
  ...
  { "hour": 23, "temperature": "16", "condition": "Cloudy" }
]
```

2) modifying one or more existing key: access to field has changed  from e.g., `result["Weather"][0]["hour"]` to `result["Weather"][0]["hour"]`

```
{
  "Weather": [
  { "hr": 0, "temp": "18", "cond": "Clear" },
  { "hr": 1, "temp": "17", "cond": "Clear" },
  ...
  { "hr": 23, "temp": "16", "cond": "Cloudy" }
 ]
}
```

3) modifying the format of expected result

```
{
  "Weather": [
    { "hour": "0am", "temperature": "18", "condition": "Clear" },
    { "hour": "1am", "temperature": "17", "condition": "Clear" },
    ...
    { "hour": "11pm", "temperature": "16", "condition": "Cloudy" }
 ]
}
```

### 2 Coordinating Across Multiple Frontends

You have **multiple frontend clients** some update imidiately and some take their update only every 1–2 months.
**How would you handle an API schema change across all of them safely?**


*The problem is mostly for breaking changes, non breaking changes, such as adding an extra field should not be that problematic.*

*In most cases the solution is to inform the clients on time and give them enough time to adapt to the new contract, keeping during that period of time both old and new version. In case of removing a field, one can mark that field as deprecated in the contract. Another possible solutions is to use API versioning (for example specifying the verion in the url) although this implies a larger effort in maintenance. *


### 3 How to Catch Breaking Changes During Development

Describe how a team can **detect breaking changes early**, in your experince. please elaburate.

*The first thing is to perform comparisons between the old and new schema and perform some analysis on what might be a breaking changes (as a conservative measure, all non additive changes can be breaking). In my experience having an extensive set of unit tests is on the fields specified by the contract is a good way. If a key, field, or format is changed in the response hopefully that will make the unit test fail. I found a TDD approach a good onae, since you start writing tests before source code development, so unbiased on any implementation but looking only at the contract. For example once it's decided a given field should be part of a response, than write the write a unit test for that.*


### 4 Policy for Releasing Changes

What internal **policy/process** was established to manage schema changes safely, in your previous team?

*The process implied treating the Schema file as source code and versioning it (Infrastructure as Code). Changes to it would got through the MR review process.*

## 🧪 Acceptance Criteria
- Answer these four questions thoroughly – at least one paragraph each, maximum half a page.
- Provide practical examples from your own experience. Don’t just rely on ChatGPT’s first suggestion — dig deeper!





