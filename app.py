from flask import Flask, render_template, request
from functions import plus, sub, multiplication, divide
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

    return render_template('index.html', result=result)

@app.route("/get/sub", methods=["GET"])
def get_sub(result=None):
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))

    result = str(sub(n1,n2))

    return render_template('index.html', result=result)

@app.route("/get/multiplication", methods=["GET"])
def get_multiplication(result=None):
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))

    result = str(multiplication(n1,n2))

    return render_template('index.html', result=result)

@app.route("/get/divide", methods=["GET"])
def get_divide(result=None):
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))

    if n2 != 0:
        result = str(divide(n1,n2))
    else:
        result = None

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
