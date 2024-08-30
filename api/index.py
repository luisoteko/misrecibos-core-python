import dataclasses
from flask import Flask, render_template, request
import api.models as models
import service as service
import xmltodict

app = Flask(__name__)


@app.route("/api/")
def hello_world():
    return render_template("index.html")


@app.route("/api/invoice", methods=["POST"])
def invoice():
    # Get the sent file
    file = request.files["file"]
    # Parse the file

    ddict = xmltodict.parse(service.open_file_storage(file))

    invoice: models.Invoice = models.Root.from_dict(ddict).invoice

    if request.accept_mimetypes.best == "application/json":
        return dataclasses.asdict(invoice)

    return render_template("invoice.html", invoice=invoice)
