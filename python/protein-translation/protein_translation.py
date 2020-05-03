def proteins(strand):
    strands = dict({
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP'
    })
    n = 3
    parts = [strand[i:i+n] for i in range(0, len(strand), n)]
    names = []
    # import pdb; pdb.set_trace()
    for part in parts:
        if strands[part] == 'STOP':
            break
        else:
            if strands.get(part, False) and strands[part] not in names:
                names.append(strands[part])

    return names
