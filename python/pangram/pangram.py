import string


def is_pangram(sentence):
    return set(list(string.ascii_lowercase)).issubset(set(list(sentence)))

