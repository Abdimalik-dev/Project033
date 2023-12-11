import json
import re
import requests
import sys
import webbrowser
from urllib.parse import quote
def custom_block(block):
    """Formatting for a custom My Block"""
    proccode = block["mutation"]["proccode"].replace("%s", "{}").replace("%b", "{}")
    placeholders = re.findall("%[sb]", block["mutation"]["proccode"])
    inputs = json.loads(block["mutation"]["argumentids"])
    for i, input_id in enumerate(inputs):
        if input_id not in block["inputs"]:
            block["inputs"][input_id] = [1, [10, ""]] if placeholders[i] == "%s" else [1, ["BOOL", ""]]
    return proccode,
OPEN_IN_BROWSER = True

def custom_block(block):
    """Formatting for a custom My Block"""
    proccode = block["mutation"]["proccode"].replace("%s", "{}").replace("%b", "{}")
    placeholders = re.findall("%[sb]", block["mutation"]["proccode"])
    inputs = json.loads(block["mutation"]["argumentids"])
    for i, input_id in enumerate(inputs):
        if input_id not in block["inputs"]:
            block["inputs"][input_id] = [1, [10, ""]] if placeholders[i] == "%s" else [1, ["BOOL", ""]]
    return proccode,
def custom_block(block):
    """Formatting for a custom My Block"""
    proccode = block["mutation"]["proccode"].replace("%s", "{}").replace("%b", "{}")
    placeholders = re.findall("%[sb]", block["mutation"]["proccode"])
    inputs = json.loads(block["mutation"]["argumentids"])
    for i, input_id in enumerate(inputs):
        if input_id not in block["inputs"]:
            block["inputs"][input_id] = [1, [10, ""]] if placeholders[i] == "%s" else [1, ["BOOL", ""]]
    return proccode, inputs
def custom_block(block):
    """Formatting for a custom My Block"""
    proccode = block["mutation"]["proccode"].replace("%s", "{}").replace("%b", "{}")
    placeholders = re.findall("%[sb]", block["mutation"]["proccode"])
    inputs = json.loads(block["mutation"]["argumentids"])
    for i, input_id in enumerate(inputs):
        if input_id not in block["inputs"]:
            block["inputs"][input_id] = [1, [10, ""]] if placeholders[i] == "%s" else [1, ["BOOL", ""]]
    return proccode,

FIELDS = {
    "_mouse_": "mouse-pointer",
    "_random_": "random position",
    "PAN": "pan left/right",
}

