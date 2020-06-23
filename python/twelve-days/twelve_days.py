def recite(start_verse, end_verse):
    days = (
        ('first', 'and a Partridge in a Pear Tree'),
        ('second', 'two Turtle Doves'),
        ('third', 'three French Hens'),
        ('fourth', 'four Calling Birds'),
        ('fifth', 'five Gold Rings'),
        ('sixth', 'six Geese-a-Laying'),
        ('seventh', 'seven Swans-a-Swimming'),
        ('eighth', 'eight Maids-a-Milking'),
        ('ninth', 'nine Ladies Dancing'),
        ('tenth', 'ten Lords-a-Leaping'),
        ('eleventh', 'eleven Pipers Piping'),
        ('twelfth', 'twelve Drummers Drumming')
    )

    output = []

    for num in range(start_verse, end_verse + 1):
        message = f"On the {days[num - 1][0]} day of Christmas my true love gave to me:"  # noqa E501

        items = [days[i][1] for i in reversed(range(num))]
        message2 = ", ".join(items)

        if num == 1:
            message2 = message2.replace('and ', '')

        output.append(f"{message} {message2}.")

    return output
