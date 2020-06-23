import itertools
from itertools import Iterable

return_array = []

def really_flatten(iterable):
    for i in iterable:
        flatten(i)
    return return_array

def flatten(iterable):
    for i in iterable:
        if isinstance(i, Iterable):
            return_array.append(list(itertools.chain.from_iterable(iterable)))
        else:
            return_array.append(i)
