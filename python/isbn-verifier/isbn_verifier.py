def is_valid(isbn):
    chunks = list(isbn.replace("-", ""))
    if len(chunks) != 10:
        return False

    if not chunks[-1].isdigit() and chunks[-1].upper() == 'X':
        chunks[-1] = '10'

    count = 10
    total = 0
    for chunk in chunks:
        if not chunk.isdigit():
            return False
        total = total + (int(chunk) * count)
        count = count -1

    return total % 11 == 0
