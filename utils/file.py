import json
from typing import BinaryIO


def get_dict_from_arb_file(file: BinaryIO) -> dict:
    """
    Arb file to dict

    :param file: arb file object
    :return: arb file as dict
    """
    return json.load(file)
