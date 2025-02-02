# Number Classification API

This API classifies a number and returns its mathematical properties along with a fun fact.

## Endpoint
GET /api/classify-number?number=371


## Example Response

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "class_sum": 11,
  "fun_fact": "371 is a narcissistic number."
}

## Deployment
Deployed on Vercel: https://number-classification-58cjsakoc.vercel.app