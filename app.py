from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number

def digit_sum(number):
    return sum(int(d) for d in str(number))

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Input validation
    if not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")
    
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math")
    fun_fact = fun_fact_response.text

    return jsonify({
        "number": number,
        "is_prime": all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)) and number > 1,
        "is_perfect": number == sum(i for i in range(1, number) if number % i == 0),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)