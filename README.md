# Number Classification API

## Overview
The **Number Classification API** is a Flask-based web service that classifies numbers based on their mathematical properties. It determines whether a number is prime, perfect, Armstrong, even, or odd. Additionally, it provides a sum of its digits and an interesting fun fact if applicable.

## Features
- **Prime Number Check**: Determines if a number is prime.
- **Perfect Number Check**: Identifies perfect numbers.
- **Armstrong Number Check**: Checks if a number is an Armstrong number.
- **Even/Odd Classification**: Determines whether a number is even or odd.
- **Digit Sum Calculation**: Computes the sum of the digits of the given number.
- **Fun Fact Generation**: Provides a unique fun fact for Armstrong numbers.

## API Endpoints
### 1. Home Route
**Endpoint:** `/`
- **Method:** GET
- **Response:** A welcome message with instructions on how to use the API.

### 2. Number Classification Route
**Endpoint:** `/api/classify-number`
- **Method:** GET
- **Query Parameter:** `number` (Required)
- **Response:** JSON containing classification details of the number.

#### Example Request
```
GET /api/classify-number?number=153
```

#### Example Response
```json
{
  "number": 153,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 9,
  "fun_fact": "153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153"
}
```

## Installation & Setup
### Prerequisites
- Python 3.x
- Flask
- Flask-CORS

### Installation Steps
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies:
   ```sh
   pip install flask flask-cors
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. The API will be accessible at:
   ```
   http://127.0.0.1:5000/
   ```

## Deployment
For production deployment, consider using **Gunicorn** or deploying via **Docker** or **Heroku**.

## Error Handling
- If an invalid input is provided, the API returns a `400 Bad Request` with an appropriate error message.
- Example:
  ```json
  {
    "number": "abc",
    "error": "Invalid input. Please provide a valid number."
  }
  ```

## License
This project is licensed under the MIT License.

---

Developed with ❤️ using Flask.

