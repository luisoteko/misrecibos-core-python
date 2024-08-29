import dataclasses
from flask import Flask, request
import models
import service

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/invoice", methods=["POST"])
def invoice():
    # Get the sent file
    file = request.files["file"]
    # Parse the file
    # app.logger.info(f"Received file: {file.filename}")
    invoice: models.Invoice = service.parse_invoice(service.open_file_storage(file))
    return dataclasses.asdict(invoice)
