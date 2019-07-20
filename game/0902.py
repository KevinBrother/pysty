# 扑克牌，给玩家发，并按照花色和大小排
from random import shuffle

class Card(object):
    __slots__ = ('_num', '_color')

    def __init__(self, num, color):
        if num == 1:
            self._num = 'A'
        elif num == 11:
            self._num = 'J'
        elif num == 12:
            self._num = 'Q'
        elif num == 13:
            self._num = 'K'
        else:
            self._num = str(num)

        if color == 1:
            self._color = '♠'
        elif color == 2:
            self._color = '♥'
        elif color == 3:
            self._color = '♣'
        else:
            self._color = '♦'

    @property
    def color(self):
        return self._color

    @property
    def num(self):
        return self._num        

        
    def __str__(self):
        return '%s%s' %  (self._num, self._color)
        
    def __repr__(self):
        return self.__str__()


class Poker(object):

    def __init__(self):
        self._cards = [Card(num, color)
                        for num in range(1, 14)
                        for color in range(1, 5)]
        self._count = 0

    @property
    def cards(self):
        return self._cards
    

    def shuffleCard(self):
        shuffle(self._cards)

    @property
    def next(self):
        # 发牌
        card = self._cards[self._count]
        self._count += 1
        return card

class Person(object):
    
    def __init__(self, name):
        self._name = name
        self._cards = []

    @property
    def cards_on_hand(self):
        return self._cards

    def get_cards(self, card):
        self._cards.append(card)

    # 排序手牌
    def arrange(self, card_key):
        self.cards_on_hand.sort(key=card_key)

def get_key(card):
    return (card.color, card.num)


def main():
    # 几个玩家
    per1 = Person('张三')
    pers = [Person('李四'), Person('王五'), Person('赵六')]
    pers.append(per1)

    # 一副牌  打乱 然后发牌
    poker = Poker()
    poker.shuffleCard()
    # print(poker.cards)

    # 随机分配牌
    for i in range(13):
        for per in pers:
            per.get_cards(poker.next)
    
    per1.arrange(get_key)
    print(per1.cards_on_hand)

    # 打印各个玩家拥有的牌

if __name__ == "__main__":
    main()