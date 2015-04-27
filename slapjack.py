#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Game of SlapJack
26 / 04 / 2015
'''
from __future__ import unicode_literals, division
import sys, random, time, thread
from curtsies import Input, fmtstr
from curtsies.fmtfuncs import *
import curtsies.events


class Frame(curtsies.events.ScheduledEvent):
    pass

class Game(object):

    def __init__(self):
        self.d = Deck()
        self.d.makeDeck()
        self.score = []

    def tick(self):
        self.d.draw()

    def process_event(self, e):
        # put logic for scoring and stuff
        if e == u'<Ctrl-j>':
            slapCard = self.d.played_cards.pop()
            if slapCard.rank != u'J':
                print 'Not a Jack'
                self.score = []
            else:
                self.score.append(len(self.d.played_cards))
                print 'Slapped %d' % sum(self.score)
                self.player_hand = self.d.played_cards
                self.d.played_cards = []


class Card(object):
    '''Generates a card with a suit, rank'''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __unicode__(self):
        if self.suit ==  u'♥' or self.suit == u'♦':
            self.suit = red(self.suit)
            return "%s%s" % (self.rank, self.suit)
        return "%s%s" % (self.rank, self.suit)

    def __str__(self):
        return unicode(self).encode('utf-8')

class Deck(object):

    def __init__(self):
        self.deck = []
        self.played_cards = []
        self.endgame = False

    def makeDeck(self):
        '''Generates a deck of 52 cards of Card objects'''

        ranks = [u'A', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'10', u'J', u'Q', u'K']
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        uniSuits = [u'♠', u'♥', u'♦', u'♣']
        for suit in uniSuits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        return self.deck

    def draw(self):
        '''selects card to be played from deck'''

        random.shuffle(self.deck)
        try:
            card = self.deck.pop()
            self.played_cards.append(card)
            print card
        except IndexError:
            self.endgame = True

def play():
    game = Game()
    dt = 1/2

    reactor = Input()
    schedule_next_frame = reactor.scheduled_event_trigger(Frame)
    schedule_next_frame(when=time.time())

    with reactor:
        for e in reactor:
            if game.d.endgame == True:
                print 'Final Score: %d' % sum(game.score)
                sys.exit()
            if isinstance(e, Frame):
                game.tick()
                when = e.when + dt
                while when < time.time():
                    when += dt
                schedule_next_frame(when)

            elif e == u'<ESC>':
                break

            else:
                game.process_event(e)

play()
