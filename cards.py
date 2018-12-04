#! /usr/bin/python

import sys
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def display(self):
        sys.stdout.write(self.rank + self.suit + ' ')

    def value(self):
        if self.rank == "A":
            return 14
        elif self.rank == "K":
            return 13
        elif self.rank == "Q":
            return 12
        elif self.rank == "J":
            return 11
        else:
            return int(self.rank)

    def __lt__(self,other):
        me = self.value()
        it = other.value()
        return( me < it )

    def __gt__(self,other):
        me = self.value()
        it = other.value()
        return( me > it )

    def __eq__(self,other):
        me = self.value()
        it = other.value()
        return( me == it )

    def __str__(self):
        return "{0}{1}".format(self.rank, self.suit)

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def take(self, card):
        if isinstance(card, Card) :
            self.cards.append(card)
        elif isinstance(card, Hand):
            self.cards = self.cards + card.cards
    
    def display(self):
        for item in self.cards:
            item.display()
        sys.stdout.write('\n')

    def __str__(self):
        rep = ""
        for item in self.cards:
            rep += str(item) + " "
        return rep

    def isEmpty(self):
        if len(self.cards) > 0:
            return 0
        elif len(self.cards) == 0:
            return 1
        else :
            print("something wrong")
            exit(1)

    def play(self):
        return self.cards.pop(0)

    def __add__(self, other):
        return Hand(self.cards + other.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def copy(self):
        ret = Hand([])
        ret = ret + self
        return ret

    def clear(self):
        self.cards = []


class Deck:
    def __init__(self):
        self.cards = []
        for r in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"):
            for s in ( "C", "D", "H", "S"):
                card = Card(r,s)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)

    def isEmpty(self):
        if len(self.cards) > 0:
            return 0
        else:
            return 1
