import random

class Card(object):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} {}".format(self.value, self.suit))

class Deck(object):
    
    def __init__(self):
        self.cards = []
        self.build()     

    def build(self):
        for s in ["Kier", "Karo", "Pik", "Trefl"]:
            for v in range(1,14):
                self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()
        



my_deck = Deck()
my_deck.shuffle()

card = my_deck.draw()
card.show()

