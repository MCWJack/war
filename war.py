#! /usr/bin/python

import cards

def finish(who):
#    p1start.display()
#    p2start.display()
    p1points = 0
    p2points = 0
    p1aces = 0
    p2aces = 0
    for card in p1start.cards :
        p1points += card.value()-1
        if card.value() == 14 :
            p1aces += 1
    for card in p2start.cards :
        p2points += card.value()-1
        if card.value() == 14 :
            p2aces += 1
    if who == "p1":
        print( str(p1points) +"\t"+ str(p1aces) +"\t"+ "p1" )
    elif who == "p2":
        print( str(p2points) +"\t"+ str(p2aces) +"\t"+ "p2" )
    else:
        print( "Error." )
    exit(0)

def play(player) :
    global p1, p2, p1Winnings, p2Winnings
    if player == "p1" :
        if p1.isEmpty() :
            if p1Winnings.isEmpty() :
                finish("p2")
            else:
                p1Winnings.shuffle()
                p1 = p1Winnings.copy()
                p1Winnings.clear()
        return p1.play()
    else :
        if p2.isEmpty() :
            if p2Winnings.isEmpty() :
                finish("p1")
            else:
                p2Winnings.shuffle()
                p2 = p2Winnings.copy()
                p2Winnings.clear()
        return p2.play()

def war():
    global p1, p2, kitty
    kitty.take(play("p1"))
    kitty.take(play("p2"))
    kitty.take(play("p1"))
    kitty.take(play("p2"))
    k1 = play("p1")
    k2 = play("p2")
    kitty.take(k1)
    kitty.take(k2)
    if k1>k2 :
        p1Winnings.take(kitty)
        kitty.clear()
        return 1
    elif k2>k1 :
        p2Winnings.take(kitty)
        kitty.clear()
        return 1
    else :
        return 0
        
###############################################################################
# Start
###############################################################################

p1 = cards.Hand([])
p2 = cards.Hand([])

p1Winnings = cards.Hand([])
p2Winnings = cards.Hand([])

deck = cards.Deck()
deck.shuffle()

while not deck.isEmpty() :
    p1.take(deck.deal())
    p2.take(deck.deal())

p1start = p1.copy()
p2start = p2.copy()

ctr = 0
while(1) :
    ctr += 1
    w = 0
    kitty = cards.Hand([])
    k1 = play("p1")
    k2 = play("p2")
    kitty.take(k1)
    kitty.take(k2)    
    if k1 > k2 :
        p1Winnings.take(kitty)
        kitty.clear()
    elif k1 < k2 :
        p2Winnings.take(kitty)
        kitty.clear()
    else :
        x = 1
        while x > 0 :
            x = war()
            w += 1
#            print w























