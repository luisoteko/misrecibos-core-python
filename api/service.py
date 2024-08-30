import zipfile
from bs4 import BeautifulSoup
import werkzeug
import werkzeug.datastructures


def safe_find(element: BeautifulSoup, tag: str):
    try:
        return element.find(tag)
    except AttributeError:
        return None


def open_file(
    file_path: str, file=None, type="S"
) -> str:  # S for standalone, F for flask
    if type == "S":
        file = file_path
    if file_path.endswith(".zip"):
        with zipfile.ZipFile(file, "r") as zip_ref:
            # read the only one xml file in the zip with functional proggramming
            file = BeautifulSoup(
                zip_ref.read(
                    list(filter(lambda x: x.endswith(".xml"), zip_ref.namelist()))[0]
                ),
                "xml",
            )
    elif file_path.endswith(".xml"):
        if type == "S":
            file = BeautifulSoup(open(file, "r", encoding="utf8"), "xml")
        else:
            file = BeautifulSoup(file.read(), "xml")
    else:
        raise ValueError("Invalid file type")
    if (file.find("Invoice") is not None) or (file.find("CreditNote") is not None):
        return str(file)
    return file.find("cac:Attachment").find("cbc:Description").text


def open_file_storage(
    file: werkzeug.datastructures.FileStorage,
) -> str:  # comming from flask
    return open_file(file.filename, file, "F")
