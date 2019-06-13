from collections import namedtuple


Card = namedtuple('Card', ['rank', 'suit'])  # 纸牌有 等级 与 花色


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    card = FrenchDeck()
    print(card[2].rank)
    print(card[2].suit)
