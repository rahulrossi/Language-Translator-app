from translate import Translator

try:
    with open("test.txt", 'r', encoding='utf-8') as my_file:
        text = my_file.read()
        translator = Translator(to_lang = "ko")
        translation = translator.translate(text)
        with open("test-ko.txt",'w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('Check your file path')
    
## We can change the language using ISO 639-1 codes in https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

# Output will be printed to 'test-ko.txt'.

"""
Translate는 파이썬으로 작성된 간단하지만 강력한 번역 도구로, 여러 번역 제공업체를 지원합니다.
현재 Microsoft Translation API 및 Translated MyMemory API와 통합되어 있습니다.
"""
