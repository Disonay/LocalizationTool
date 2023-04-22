import json


def get_dict_from_arb_file(file) -> dict:
    return json.load(file)
