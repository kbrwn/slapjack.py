#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Game of SlapJack
'''
import sys, random, time
#colorama

#Class Deck
    #draw function
    #shuffle function


class Card(object):
    '''Generates a card with a suit, rank'''

    ##use class to create unicode representation

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return unicode(self).encode('utf-8')

    #def __repr__(self): # should be used to reprensent data as it is inputed
        #return '%s of %s' % (self.rank.encode('utf-8'), self.suit.encode('utf-8'))

    def __unicode__(self):
        return '%s of %s' % (self.rank, self.suit)

class Deck(object):

    def __init__(self):
        self.deck = []


    def makeDeck(self):
        '''Generates a deck of 52 cards of Card objects'''

        ranks = ['A', '2', '3', '4', '5', '6','7', '8', '9', '10', 'J','Q', 'K']
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        uniSuits = [u'♠', u'♥', u'♦', u'♣']
        for suit in uniSuits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        return self.deck

    def draw(self):
        '''Prints a card from deck if it hasn't been played before'''

        random.shuffle(self.deck)
        card = self.deck.pop()
        print card


def timed_print():
    '''prints out a card every half-second'''
    for i in range(52):
        time.sleep(0.4)
        print_card()

d = Deck()
d.makeDeck()


def input_thread(L):
#function to use in the thread that waits for input
    raw_input()
    L.append(None) # list that will be appended if player hits a key ()"slaping")

def printdeck():
#function to print deck
    L = []
    thread.start_new_thread(input_thread, (L,)) #this thread is waiting for user input
    while True:
            timed_print()
            if L:
                print "You Slapped!"
                L.pop()


initdeck()
printdeck()
