#!/usr/bin/env python3
from googletrans import Translator

translator = Translator()
print(translator.translate('Hello', src='en', dest='ja').text)