from flask import Flask, render_template, request
from functions import plus, sub, multiplication, divide, square, sqrt
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200

@app.route("/get/plus", methods=["GET"])
def get_plus(result=None):
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))

    result = str(plus(n1,n2))

    return result

@app.route("/get/sub", methods=["GET"])
def get_sub(result=None):
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))
    
    result = str(sub(n1,n2))

    return result

@app.route("/get/multiplication", methods=["GET"])
def get_multiplication(result=None):
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))

    result = str(multiplication(n1,n2))

    return result

@app.route("/get/divide", methods=["GET"])
def get_divide(result=None):
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))

    if n2 != 0:
        result = str(divide(n1,n2))
    else:
        result = None

    return result

@app.route("/get/square", methods=["GET"])
def get_square(result=None):
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))

    return str(square(n1,n2))

@app.route("/get/sqrt", methods=["GET"])
def get_sqrt(result=None):
    n1 = float(request.args.get('n1'))
    if n1 < 0:
        return "Please enter a number greater than or equal to 0."
    else:
        return str(sqrt(n1))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
