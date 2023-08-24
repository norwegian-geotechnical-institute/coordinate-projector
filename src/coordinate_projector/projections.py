from typing import Dict, Any
import json
import os

projections: Dict[Any, Any] = {}

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "projections.json")

with open(file_path, "r") as json_file:
    data = json.load(json_file)
    projections = data
