import translators.server as ts

from consts.translate import NOT_TRANSLATABLE_KEYS, API_NAME


def translatable_key(key: str) -> bool:
    """
    Checks if it is necessary to translate the value of this key. For example,
    the key "format" containing the date format does not need to be translated

    :param key: key from dict
    :return: true if translatable and false if not
    """
    return key not in NOT_TRANSLATABLE_KEYS


def translate_str(source_lang: str, target_lang: str, source: str, api_name=API_NAME) -> str:
    """
    Translate string from source language to target language

    :param source_lang: original language
    :param target_lang: language after translation
    :param source: string to be translated
    :param api_name: translation api (google, bing, deepl, etc)
    :return: translated string
    """
    translator = getattr(ts, api_name)

    return translator(source, from_language=source_lang, to_language=target_lang)


def translate_dict_values(source_lang: str, target_lang: str, source: dict, api_name=API_NAME):
    """
    Translate string values of dict from source language to target language

    :param source_lang: original language
    :param target_lang: language after translation
    :param source: dict whose values must be translated
    :param api_name: translation api (google, bing, deepl, etc)
    """
    if isinstance(source, dict):
        for key, value in source.items():
            if isinstance(value, str) and translatable_key(key):
                source[key] = translate_str(source_lang, target_lang, value, api_name)
            else:
                translate_dict_values(source_lang, target_lang, value, api_name)
    if isinstance(source, list):
        for index, value in enumerate(source):
            if isinstance(value, str):
                source[index] = translate_str(source_lang, target_lang, value, api_name)
            else:
                translate_dict_values(source_lang, target_lang, value, api_name)
