def is_isogram(string):
    for ch in string:
        if ch =='-' or ch == ' ':
            continue
        if string.lower().count(ch) > 1:
            return False

    return True
