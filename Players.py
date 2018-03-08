"""players.py: 

Players.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os

class Player( ):

    def __init__(self, id, loc, type = 'HINTER' ):
        self.id = id
        self.location = loc
        self.type = 'HINTER' if id % 2 == 0 else 'GUESSER'
        self.penaltyPile = [ ]
        self.nTurns = 0

    def add2penaly( self, c ):
        if isinstance( c, list ):
            self.penaltyPile += c
        else:
            self.penaltyPile.append( c )

    def __str__( self ):
        return '  P%s: %s' % (self.id, ' '.join(map(str,self.penaltyPile)))
