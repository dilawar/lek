#!/usr/bin/env python3

"""lek.py: 

"""

from __future__ import print_function
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import logging
import itertools
import random
from globals import *

def is_grid_valid( ):
    # At least 3 card must be valid for rule.
    res = list( map(is_valid_card, grid_ ) )
    validCount = res.count( True )
    if validCount >= 3:
        return True
    return False

def step( i ):
    print_grid( )
    print_players( )
    print( '===================' )

def play( args ):
    print( rule_ )
    init_chain( )
    print_grid( )
    print_chain( chain_ )
    assert is_grid_valid( ), "Grid does not have at least 3 valid card"
    for i in itertools.count( ):
        curTeam = i % 2
        print( '[INFO] Team %d' % (1+curTeam) )
        g, h = players_[ 2*curTeam:(2*curTeam+2) ]

        g.nTurns += 1
        cs = input( 'GUESSER pick card(s) from grid [1-9]?' )
        ps = [ int(c) - 1 for c in cs.split( ) ]
        cards = pick_cards_from_grid( ps[:3] )
        print( '- You picked: %s' % cards )
        nValids = list(map(is_valid_card, cards)).count( True )

        if nValids == len(cards):
            print( '- Congrats. You have valid card (s)' )
        else:
            print( '- Invalid card(s) in picked cards' )

        # HINTER picks
        if len( cards ) == 1:
            h.nTurns += 1
            vs = hinter_pick_max3_cards_from_grid( )
            h.add2penaly( vs )

        print( 'Grid' )
        print_grid( )
        print( 'Chain' )
        print_chain( )
        print( 'Players' )
        print_players( )

def main( args ):
    play( args )

if __name__ == '__main__':
    import argparse
    # Argument parser.
    description = '''Game of LEK.'''
    parser = argparse.ArgumentParser(description=description)
    class Args: pass 
    args = Args( )
    parser.parse_args(namespace=args)
    main( args )
