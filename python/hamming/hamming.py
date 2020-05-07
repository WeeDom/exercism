def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strands must have equal lengths")
    return sum(val1 != val2 for val1, val2 in zip(strand_a, strand_b))
