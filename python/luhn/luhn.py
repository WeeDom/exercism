class Luhn():
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')[::-1]

    def valid(self):
        card_num = self.card_num
        if not card_num.isdigit() or len(card_num) <= 1:
            return False
        else:
            luhn = 0
            for i, num in enumerate(card_num):
                num = int(num)
                if i % 2:
                    num = num * 2 - 9 if num * 2 > 9 else num * 2
                luhn += num

        return (luhn % 10) == 0
