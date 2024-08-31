import dataclasses
import logging
from flask import Flask, render_template, request
import api.models as models
import api.service as service
import xmltodict

app = Flask(__name__)


@app.route("/api/index")
def hello_world():
    return render_template("index.html")


@app.route("/api/invoice", methods=["POST"])
def invoice():
    # Get the sent file
    file = request.files["file"]
    # Parse the file
    try:
        ddict = xmltodict.parse(service.open_file_storage(file))
    except ValueError as e:
        return {'errorMessage': str(e)}, 406

    invoice: models.Root = models.Root.from_dict(ddict)

    if request.accept_mimetypes.best == "application/json":
        return dataclasses.asdict(invoice)

    return render_template("invoice.html", invoice=invoice)
