from flask import Flask, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


@app.route("/health")
def health():
    return jsonify(status="ok")
