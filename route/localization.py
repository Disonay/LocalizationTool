from fastapi import APIRouter

from data.json_request import ArbJsonRequest
from translation.translation_func import translate_dict_values

router = APIRouter(prefix="/localization", tags=["Localization"])


@router.post("/local-from-json")
def local_from_json(data: ArbJsonRequest, source_lang: str = "en", target_lang="ru") -> dict:
    translate_dict_values(source_lang, target_lang, data.payload)

    return data.payload
