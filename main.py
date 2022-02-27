class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build()
    def build(self):
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            print(s)
            for v in range(2,11):
                self.cards.append(Card(s,v))
            for v in ["ace","king","queen","jack"]:
                self.cards.append(Card(s,v))
    def show(self):
        for c in self.cards:
            c.show()

class Player:
    pass
deck = Deck()

