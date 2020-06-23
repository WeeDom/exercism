import string

import re

CIPHER = 'zyxwvutsrqponmlkjihgfedcba'
ENCODE = str.maketrans(CIPHER, string.ascii_lowercase)
DECODE = str.maketrans(string.ascii_lowercase, CIPHER)
PUNC = str.maketrans('', '', string.punctuation)


def encode(plain_text):
    plain_text = re.findall('.{1,5}', plain_text.lower().replace(" ", "").translate(PUNC).translate(ENCODE))  # noqa E501
    return ' '.join(plain_text)


def decode(ciphered_text):
    return ciphered_text.translate(DECODE).replace(" ", "")
