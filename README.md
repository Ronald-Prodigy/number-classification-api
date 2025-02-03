# Number Classification API

## Description
The **Number Classification API** is a simple web service that classifies numbers based on mathematical properties and provides an interesting fun fact about the number.

## Features
- Identifies whether a number is **prime**, **Armstrong**, **even**, or **odd**.
- Computes the **sum of digits** of the number.
- Fetches a **fun fact** about the number using [Numbers API](http://numbersapi.com).
- Returns responses in **JSON format**.
- Handles **input validation** and **error responses**.

## API Endpoint
### **GET** `/api/classify-number?number=<integer>`

#### **Example Request:**
```sh
curl "http://your-deployed-url/api/classify-number?number=371"
```

#### **Example Successful Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Error Response (400 Bad Request):**
```json
{
    "number": "invalid_input",
    "error": true
}
```

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/number-classifier-api.git
cd number-classifier-api
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Run the API Locally**
```sh
python app.py
```

The API will be accessible at `http://127.0.0.1:5000/api/classify-number`.

## Deployment
You can deploy this API using any cloud platform:
- **Render** ([Render.com](https://render.com))
- **Railway** ([Railway.app](https://railway.app))
- **AWS/GCP/Azure**





