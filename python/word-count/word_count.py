import re
from collections import defaultdict


def count_words(sentence):
    for char in '_-.,\n:!&@$%^&':
        sentence = sentence.replace(char, ' ')
    sentence = sentence.lower()
    word_count = defaultdict(int)
    for w in sentence.split():
        word_count[re.sub(r'^["\']{1,}|["\']{1,}$', '', w)] += 1

    return word_count
