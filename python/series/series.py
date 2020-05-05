def slices(series, length):
    integers = list(series)
    # import pdb; pdb.set_trace()
    if len(integers) < length or length <= 0:
        raise ValueError("bad input")
    orig_length = length
    res = []
    for i in range(0, len(integers)):
        if len(integers[i:length]) == orig_length:
            res.append(''.join(list(map(str, integers[i:length]))))
        length += 1

    return res
