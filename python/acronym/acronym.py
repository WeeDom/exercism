import string
import re


def abbreviate(words):
    return ''.join(word[0].upper() for word in ' '.join(re.split(r'[\s-]', words)).translate(str.maketrans('', '', string.punctuation)).split()) # noqa E128
