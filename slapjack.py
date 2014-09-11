import random

deck = {}

faces = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',\
  'Seven', 'Eight', 'Nine', 'Ten', 'Jack',\
  'Queen', 'King']

suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

def initdeck():
    #x = deck.get()
    for i in range(52):
        card_face = random.choice(faces)
        card_suit = random.choice(suits)
        deck[0] = (card_suit,card_face)

        if (card_suit,card_face) in deck:
            break
        else:
            deck[i] = (card_suit,card_face)


    print 'deck =', deck

initdeck()
