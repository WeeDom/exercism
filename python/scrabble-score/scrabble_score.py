scrabble_scores = [
    (1, "E A O I N R T L S U"),
    (2, "D G"),
    (3, "B C M P"),
    (4, "F H V W Y"),
    (5, "K"),
    (8, "J X"),
    (10, "Q Z")
    ]
LETTER_SCORES = {
    letter: score for score, letters
    in scrabble_scores for letter in letters.split()
    }


def score(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = []
    for char in word:
        if char in ['-']:
            return 0
        else:
            score.append(LETTER_SCORES[char.upper()])

    return sum(score)
