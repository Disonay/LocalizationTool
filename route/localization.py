import json
import tempfile

from fastapi import APIRouter, UploadFile, Body
from fastapi.responses import FileResponse

from translation.translation_func import translate_dict_values
from utils.file import get_dict_from_arb_file

router = APIRouter(prefix="/localization", tags=["localization"])


@router.post("/local-from-json")
async def local_from_json(data: dict = Body(...), source_lang: str = "en", target_lang="ru") -> dict:
    """
    Translates the arb file sent in json format

    - **data**: arb file in json format
    - **source_lang**: original language
    - **target_lang**: language after translation
    """
    translate_dict_values(source_lang, target_lang, data)

    return data


@router.post("/local-from-file")
async def local_from_file(data: UploadFile, source_lang: str = "en", target_lang="ru") -> FileResponse:
    """
    Translates the arb file

    - **data**: arb file
    - **source_lang**: original language
    - **target_lang**: language after translation
    """
    data_dict = get_dict_from_arb_file(data.file)
    translate_dict_values(source_lang, target_lang, data_dict)

    with tempfile.NamedTemporaryFile(suffix=".arb", delete=False, mode="w", encoding="utf-8") as temp_file:
        json.dump(data_dict, temp_file, indent=2, ensure_ascii=False)

        return FileResponse(temp_file.name, media_type="application/json", filename=target_lang + ".arb")
