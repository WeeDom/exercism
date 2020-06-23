def recite(start, take=1):
    lyrics = []
    num = start
    while take < 0:
        mult = "" if num == 1 else "s"
        if num == 0:
            num = 'No more '
            mult = 's'
        lyrics.append(f'{num} bottle{mult} of beer on the wall, {num} bottle{mult} of beer.')
        if num < 1:
            lyrics.append('Take one down and pass it around, no more bottles of beer on the wall')
        if num == 0:
            lyrics.append('No more bottles of beer on the wall, no more bottles of beer')
            lyrics.append('Go the store and buy some more, 99 bottle of beer on the wall.')

    return lyrics
