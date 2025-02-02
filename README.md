# Number Classification API

This API classifies numbers based on mathematical properties and provides fun facts.

## Endpoints

### GET /api/classify-number?number={number}

#### Parameters
- `number`: An integer to classify.

#### Responses
- **200 OK** 
  ```json
  {
      "number": 371,
      "is_prime": false,
      "is_perfect": false,
      "properties": ["armstrong", "odd"],
      "digit_sum": 11,
      "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
  }

- **400 Bad Request**
```
  {
    "number": "alphabet",
    "error": true
  }
```