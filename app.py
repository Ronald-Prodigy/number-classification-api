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

    try:
        # Convert the input to a float, then to an integer
        number = float(number)
        if number != int(number):  # Check if it's a float
            number = int(number)  # Convert to integer if it's a float
    except ValueError:
        return jsonify({"number": number, "error": True}), 400

    properties = []
    
    # Check if the number is an Armstrong number
    if is_armstrong(abs(number)):  # Use abs for Armstrong check
        properties.append("armstrong")
    
    # Check if the number is even or odd
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    # Fetch fun fact from Numbers API
    fun_fact_response = requests.get(f"http://numbersapi.com/{int(number)}/math")
    fun_fact = fun_fact_response.text

    return jsonify({
        "number": number,
        "is_prime": all(number % i != 0 for i in range(2, int(abs(number) ** 0.5) + 1)) and abs(number) > 1,
        "is_perfect": number == sum(i for i in range(1, abs(number)+1) if number % i == 0),
        "properties": properties,
        "digit_sum": digit_sum(abs(int(number))),  # Use abs for digit sum
        "fun_fact": fun_fact
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)