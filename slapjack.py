import random, time, thread, threading

'''
this game is a work in progress - 9/21/2014

slapjack.py

to do:

 - fix loop to prevent duplicate cards
 - thread stop printing cards
 - develop a system to count score


'''


deck = {} #this is a dictionary of 0-51. Each value has two keys.

faces = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',\
  'Seven', 'Eight', 'Nine', 'Ten', 'Jack',\
  'Queen', 'King']

suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']


def input_thread(L):
#function to use in the thread that waits for input
    raw_input()
    L.append(None) # list that will be appended if player hits a key ()"slaping")


def initdeck():
#function to initiliaze the deck of cards
    for i in range(52):
        card_face = random.choice(faces)
        card_suit = random.choice(suits)
        deck[0] = (card_suit,card_face) # initial card to be checked against

        if (card_suit,card_face) in deck: # this loop is meant to check for duplicate cards and not print them. Currently not working.
            break
        else:
            deck[i] = (card_suit,card_face)

def printdeck():
#function to print deck
    L = []
    thread.start_new_thread(input_thread, (L,)) #this thread is waiting for user input
    while True:
        for i in range(52):
            card = deck.get(i) #sudden realization that I should probably use some loop logic to prevent duplicates from being printed
            print card[1] + ' of ' + card[0]
            time.sleep(1)
            if L:
                print "You Slapped!"
                L.pop()


initdeck()
printdeck()
