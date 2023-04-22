import translators.server as ts


def translate_str(source_lang: str, target_lang: str, source: str, api_name="bing"):
    translator = getattr(ts, api_name)

    return translator(source, from_language=source_lang, to_language=target_lang)


def translate_dict_values(source_lang: str, target_lang: str, source: dict, api_name="bing"):
    if isinstance(source, dict):
        for key, value in source.items():
            if isinstance(value, str):
                source[key] = translate_str(source_lang, target_lang, value, api_name)
            else:
                translate_dict_values(source_lang, target_lang, value, api_name)
    if isinstance(source, list):
        for index, value in enumerate(source):
            if isinstance(value, str):
                source[index] = translate_str(source_lang, target_lang, value, api_name)
            else:
                translate_dict_values(source_lang, target_lang, value, api_name)
