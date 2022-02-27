import random

class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    def display(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build()
    def build(self):
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            for v in range(2,11):
                self.cards.append(Card(s,v))
            for v in ["ace","king","queen","jack"]:
                self.cards.append(Card(s,v))
    def display(self):
        for c in self.cards:
            c.display()
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def draw(self):
        return str(self.cards.pop())


deck = Deck()
deck.shuffle()


class Player:
    def __init__(self, name) -> None:
        self.hand = []
        self.name = name
    def draw(self,deck):
        self.hand.append(deck.cards.pop())
    def showhand(self):
        for card in self.hand:
            card.display()


bob = Player("Bob")
jessie = Player("Jessie")
arthur = Player("Arthur")
kurt = Player("Kurt")
for i in range(13):
    bob.draw(deck)
    jessie.draw(deck)
    arthur.draw(deck)
    kurt.draw(deck)
print(f"\nThis is {bob.name}'s Cards")
bob.showhand()
print(f"\nThis is {jessie.name}'s Cards")
jessie.showhand()
print(f"\nThis is {arthur.name}'s Cards")
arthur.showhand()
print(f"\nThis is {kurt.name}'s Cards")
kurt.showhand()


