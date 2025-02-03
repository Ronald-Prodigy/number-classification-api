from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_properties(n):
    """Get mathematical properties of the number."""
    properties = []
    if is_prime(n):
        properties.append("prime")
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def get_fun_fact(n):
    """Fetch a fun fact about the number."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}", timeout=2)
        return response.text if response.status_code == 200 else "No fun fact available."
    except requests.exceptions.RequestException:
        return "Could not retrieve fun fact."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """API endpoint to classify a number."""
    num = request.args.get('number')

    if num is None or not num.lstrip('-').isdigit():
        return jsonify({"number": num, "error": True}), 400
    
    num = int(num)
    properties = get_properties(num)
    
    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": False,  # Implement perfect number check if required
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(num)),
        "fun_fact": get_fun_fact(num)
    }
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
