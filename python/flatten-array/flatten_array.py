def flatten(iterable):
    return __nested_flat(*iterable)

def __nested_flat(*args):
    items = []
    for arg in args:
        if arg is None or arg == () or arg == {}:
            next
        elif isinstance(arg, list):
            items += flatten(arg)
        else:
            items.append(arg)
    return items
