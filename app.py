from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Helper functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) == n

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def get_parity(n):
    return "even" if n % 2 == 0 else "odd"

def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact available."

# API endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = []
    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append(get_parity(number))

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "class_sum": sum_of_digits(number),
        "fun_fact": get_fun_fact(number)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)