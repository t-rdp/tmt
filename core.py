# -*- coding: utf-8 -*-

print("Loading models....")
from translators.ja2en import translate_ja_en
from translators.en2zh import translate_en_zh
print("Finished!")

from langdetect import detect


def translate(text, target_lang, source_lang='auto'):
    if text == '':
        return ''

    if len(text) > 900:
        return '抱歉，翻译失败。错误原因：字数过长，无法翻译！'

    if source_lang == 'auto':
        source_lang = detect(text)

    if source_lang == target_lang:
        return text

    if target_lang == 'en':  # To EN
        if source_lang == 'ja':
            return translate_ja_en(text)
    elif source_lang == 'en':  # From EN
        if target_lang == 'zh':
            return translate_en_zh(text)
    else:
        return '抱歉，翻译失败。错误原因：语言不支持。' # translate(translate(text, 'en', source_lang), target_lang, 'en')

    return '抱歉，翻译失败。错误原因：未知错误！'