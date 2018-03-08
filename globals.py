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
import pydealer
import logging
import random

from Players  import Player
from Rule import Rule
from MyCard import MyCard

chain_ = [ ]
deck_ = pydealer.Deck( )
deck_.shuffle( )

def deal( n ):
    global deck_
    cards = [ MyCard(x) for x in deck_.deal(n) ]
    if n == 1:
        return cards[0]
    return cards

def pick_cards_from_grid( ps ):
    picked = [ ]
    for p in ps:
        picked.append( grid_[p] )
        grid_[p] = deal( 1 )
    return picked

def print_grid( ):
    global grid_
    for i in range( int(len(grid_)/3) ):
        print_chain( grid_[i*3:(1+i)*3] )

def print_chain( row = None ):
    global chain_
    if row is None:
        row = chain_
    row = [ '%4s' % r for r in row ]
    print( ' '.join( row ) )

def is_valid_card( c ):
    global chain_
    return rule_.eval( chain_[-1], c )

def print_players( ):
    global players_
    for p in players_:
        print( p )

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

        if is_valid_card( x ):
            logging.debug( 'Appending %s' % x )
            chain_.append( x )
        else:
            logging.debug( 'Card %s is ignored' % x )
            rejected.append( x )

    deck_.add( rejected )
    logging.info( 'Chain has been initialized' )

def hinter_pick_max3_cards_from_grid( ):
    global grid_
    validI = [ ]
    for i, c in enumerate( grid_ ):
        if is_valid_card( c ):
            validI.append( i )

    picked = [ ]
    random.shuffle( validI )
    pickI = validI[:3]
    for p in validI[:3]:
        picked.append( grid_[p] )
        grid_[p] = deal( 1 )

    return picked


players_ = [ Player(i,i) for i in range(4) ]
grid_ = deal(9) 
rule_ = Rule( '(PREV.color==red)?CUR.color==black:True' )
