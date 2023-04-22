from fastapi import APIRouter, UploadFile

from data.json_request import ArbJsonRequest
from translation.translation_func import translate_dict_values
from utils.file import get_dict_from_arb_file

router = APIRouter(prefix="/localization", tags=["Localization"])


@router.post("/local-from-json")
def local_from_json(data: ArbJsonRequest, source_lang: str = "en", target_lang="ru") -> dict:
    translate_dict_values(source_lang, target_lang, data.payload)

    return data.payload


@router.post("/local-from-file")
def local_from_file(data: UploadFile, source_lang: str = "en", target_lang="ru") -> dict:
    data_dict = get_dict_from_arb_file(data.file)
    translate_dict_values(source_lang, target_lang, data_dict)

    return data_dict
