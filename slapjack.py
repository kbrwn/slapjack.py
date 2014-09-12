import random, time


deck = {} #this is a dictionary of 0-51. Each value has two keys.

faces = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',\
  'Seven', 'Eight', 'Nine', 'Ten', 'Jack',\
  'Queen', 'King']

suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']


# Function to initiliaze the deck of cards.
#

def initdeck():
    for i in range(52):
        card_face = random.choice(faces)
        card_suit = random.choice(suits)
        deck[0] = (card_suit,card_face) # initial card to be checked against

        if (card_suit,card_face) in deck:
            break
        else:
            deck[i] = (card_suit,card_face)

def printdeck():
    for i in range(52):
        card = deck.get(i)
        print card[1] + ' of ' + card[0]
        time.sleep(1)

initdeck()
printdeck()

#print 'deck =', deck
