import dataclasses
from flask import Flask, render_template, request
import models
import service as service

app = Flask(__name__)


@app.route("/api/")
def hello_world():
    return render_template("index.html")


@app.route("/api/invoice", methods=["POST"])
def invoice():
    # Get the sent file
    file = request.files["file"]
    # Parse the file

    invoice: models.Invoice = service.parse_invoice(service.open_file_storage(file))

    if request.accept_mimetypes.best == "application/json":
        return dataclasses.asdict(invoice)

    return render_template("invoice.html", invoice=invoice)
