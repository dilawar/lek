"""MyCard.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

suit_ = { 'Diamonds' : '♢', 'Clubs' : '♣', 'Spades' : '♠', 'Hearts' : '♡' }

class MyCard( ):

    def __init__(self, c ):
        self.card = c
        self.color = 'black' if c.suit in [ 'Spades', 'Clubs' ] else 'red'

    def __repr__( self ):
        global suit_
        suit = suit_[ self.card.suit ]
        val = self.card.value[0]
        return '%s%s' % (val, suit)

