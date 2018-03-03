# -*- coding: utf-8 -*-

from __future__ import print_function
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
from Players  import Player
from Rule import Rule
import pydealer
import logging

suit_ = { 'Diamonds' : '♢', 'Clubs' : '♣', 'Spades' : '♠', 'Hearts' : '♡' }
chain_ = [ ]
deck_ = pydealer.Deck( )
deck_.shuffle( )

def deal( n ):
    cards = [ MyCard(x) for x in deck_.deal(n) ]
    if n == 1:
        cards = cards[0]
    return cards

class MyCard( ):

    def __init__(self, card ):
        self.card = card
        self.color = 'black' if self.card.suit in [ 'Spades', 'Clubs' ] else 'red'

    def __repr__( self ):
        global suit_
        suit = suit_[ self.card.suit ]
        val = self.card.value[0]
        return '%s%s' % (val, suit)

def print_grid( ):
    global grid_
    print( '---' )
    for row in grid_:
        print_chain( row )
    print( '---' )

def print_chain( row ):
    row = [ '%4s' % r for r in row ]
    print( ' '.join( row ) )

def init_chain( ):
    global chain_
    global deck_
    chain_.append( deal(1) )
    rejected = [ ]
    while len( chain_ ) < 3:
        try:
            x =  deal( 1 )
        except Exception as e:
            logging.warn( "Could not contruct the CHAIN. Is rule if fine?" )
            return None

        if rule_.eval( chain_[-1], x ):
            logging.debug( 'Appending %s' % x )
            chain_.append( x )
        else:
            logging.debug( 'Card %s is ignored' % x )
            rejected.append( x )

    deck_.add( rejected )
    logging.info( 'Chain has been initialized' )


players_ = [ Player(i,i) for i in range(4) ]
grid_ = [ deal(3) for x in range(3) ]
rule_ = Rule( '(PREV.color==red)?CUR.color==black:True' )

