"""globals.py: 

Globals

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
from Players  import Player
import pydealer

deck_ = pydealer.deck
players_ = [ Player(i,i) for i in range(4) ]
grid_ = [ [0] * 3 ] * 3
chain_ = [ ]
