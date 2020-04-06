from googletrans import Translator
import sys

# HOW TO RUN: python translator.py (file) destination language (user language abbreviation - en, de, ja...))')

translator = Translator()

try:
    with open(sys.argv[1]) as text_file:
        original_text = text_file.read()
        translation = translator.translate(original_text, dest=sys.argv[2])
        with open('translated_text.txt', 'w', encoding='utf-16') as translated_text:
            translated_text.write(translation.text)
except FileNotFoundError :
    print('File not found!')