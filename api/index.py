import dataclasses
from flask import Flask, request
import models
import service

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/invoice")
def invoice():
    # Get the sent file
    file = request.files['file']
    # Parse the file
    invoice: models.Invoice = service.parse_invoice(file)
    return dataclasses.asdict(invoice)
