# Example Outputs

## Example 1: GitHub Search + Weather

**Input:**
```
Find top 3 Python repositories and weather in San Francisco
```

**Planner Output:**
```json
{
  "task_summary": "Search for top Python repositories on GitHub and get current weather in San Francisco",
  "steps": [
    {
      "step_number": 1,
      "action": "github_search",
      "parameters": {
        "query": "language:python",
        "limit": 3,
        "sort": "stars"
      },
      "reasoning": "Find the most popular Python repositories"
    },
    {
      "step_number": 2,
      "action": "weather_current",
      "parameters": {
        "city": "San Francisco"
      },
      "reasoning": "Get current weather conditions for San Francisco"
    }
  ]
}
```

**Final Output:**
```json
{
  "task": "Find top 3 Python repositories and weather in San Francisco",
  "status": "success",
  "verification": {
    "is_complete": true,
    "missing_items": [],
    "summary": "Successfully found 3 Python repositories and current San Francisco weather",
    "confidence": "high"
  },
  "data": [
    {
      "step": 1,
      "action": "github_search",
      "data": [
        {
          "name": "system-design-primer",
          "full_name": "donnemartin/system-design-primer",
          "description": "Learn how to design large-scale systems",
          "stars": 245000,
          "language": "Python",
          "url": "https://github.com/donnemartin/system-design-primer"
        },
        {
          "name": "public-apis",
          "full_name": "public-apis/public-apis",
          "description": "A collective list of free APIs",
          "stars": 280000,
          "language": "Python",
          "url": "https://github.com/public-apis/public-apis"
        },
        {
          "name": "Python",
          "full_name": "TheAlgorithms/Python",
          "description": "All Algorithms implemented in Python",
          "stars": 175000,
          "language": "Python",
          "url": "https://github.com/TheAlgorithms/Python"
        }
      ]
    },
    {
      "step": 2,
      "action": "weather_current",
      "data": {
        "city": "San Francisco",
        "country": "US",
        "temperature": 15.5,
        "feels_like": 14.8,
        "humidity": 72,
        "weather": "Clouds",
        "description": "overcast clouds",
        "wind_speed": 4.5,
        "units": "°C"
      }
    }
  ],
  "errors": null
}
```

## Example 2: Repository Info

**Input:**
```
Get information about tensorflow/tensorflow repository
```

**Planner Output:**
```json
{
  "task_summary": "Get detailed information about the TensorFlow repository",
  "steps": [
    {
      "step_number": 1,
      "action": "github_info",
      "parameters": {
        "owner": "tensorflow",
        "repo": "tensorflow"
      },
      "reasoning": "Fetch detailed repository information"
    }
  ]
}
```

**Final Output:**
```json
{
  "task": "Get information about tensorflow/tensorflow repository",
  "status": "success",
  "verification": {
    "is_complete": true,
    "missing_items": [],
    "summary": "Retrieved complete information about TensorFlow repository",
    "confidence": "high"
  },
  "data": [
    {
      "step": 1,
      "action": "github_info",
      "data": {
        "name": "tensorflow",
        "full_name": "tensorflow/tensorflow",
        "description": "An Open Source Machine Learning Framework for Everyone",
        "stars": 182000,
        "forks": 74000,
        "language": "C++",
        "url": "https://github.com/tensorflow/tensorflow",
        "topics": ["machine-learning", "deep-learning", "tensorflow"],
        "created_at": "2015-11-07T01:19:20Z",
        "updated_at": "2025-02-04T18:32:15Z"
      }
    }
  ],
  "errors": null
}
```

## Example 3: Multi-City Weather

**Input:**
```
Get weather for London, Paris, and Tokyo
```

**Planner Output:**
```json
{
  "task_summary": "Get current weather for three cities",
  "steps": [
    {
      "step_number": 1,
      "action": "weather_current",
      "parameters": {"city": "London"},
      "reasoning": "Get London weather"
    },
    {
      "step_number": 2,
      "action": "weather_current",
      "parameters": {"city": "Paris"},
      "reasoning": "Get Paris weather"
    },
    {
      "step_number": 3,
      "action": "weather_current",
      "parameters": {"city": "Tokyo"},
      "reasoning": "Get Tokyo weather"
    }
  ]
}
```

## Example 4: Error Handling

**Input:**
```
Get weather for InvalidCityName12345
```

**Final Output:**
```json
{
  "task": "Get weather for InvalidCityName12345",
  "status": "partial_success",
  "verification": {
    "is_complete": false,
    "missing_items": ["Valid weather data"],
    "summary": "Could not retrieve weather data due to invalid city name",
    "confidence": "high"
  },
  "data": [],
  "errors": [
    {
      "step": 1,
      "action": "weather_current",
      "error": "Weather API Error: 404 city not found"
    }
  ]
}
```

## CLI Output Example

```
╔═══════════════════════════════════════════════╗
║   AI Operations Assistant                     ║
║   Multi-Agent Task Automation System          ║
╚═══════════════════════════════════════════════╝

Example tasks:
1. Find the top 3 Python repositories on GitHub and get the current weather in San Francisco
2. Search for machine learning repositories and tell me the weather in London
3. Get information about the tensorflow/tensorflow repository

Or enter your own task (or 'quit' to exit)

Enter task: 1

============================================================
TASK: Find the top 3 Python repositories on GitHub and get the current weather in San Francisco
============================================================

📋 PLANNER: Creating execution plan...
✓ Plan created with 2 steps

⚙️  EXECUTOR: Running plan steps...
✓ Executed 2 steps

✅ VERIFIER: Validating results...
✓ Verification complete

============================================================
FINAL RESULT:
============================================================

{
  "task": "Find the top 3 Python repositories...",
  "status": "success",
  "verification": {
    "is_complete": true,
    "summary": "Successfully retrieved 3 Python repositories and San Francisco weather"
  },
  "data": [...]
}

============================================================
Want to try another task? (or 'quit' to exit)
============================================================
```
