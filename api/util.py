# Main file for standalone execution
import json
import xmltodict
import os

import service as service

# Read all files in a directory
files = os.listdir("xmls")


def xml_to_json(filename):
    file = service.open_file("xmls/" + filename)
    ddict = xmltodict.parse(file)
    with open(
        "jsons/" + filename.replace("xml", "json").replace("zip", "json"), "w"
    ) as json_file:
        json.dump(ddict, json_file, indent=4)


for filename in files:
    xml_to_json(filename)
