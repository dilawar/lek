"""Screen.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import curses

class Screen( ):
    """docstring for Screen"""

    def __init__(self):
        self.stdscr = curses.initscr( )
        curses.noecho( )
        curses.cbreak( )
        self.stdscr.keypad( 1 )
        self.logWin = curses.newwin(20, 50, 30, 50 )
        self.playerWin = curses.newwin( 20, 40, 0, 30 )
        self.refresh( )

    def refresh( self ):
        self.stdscr.refresh( )

    def close( self ):
        curses.endwin( )

    def log( self, msg ):
        if isinstance( msg, list ):
            msg = '\n'.join( msg )
        self.stdscr.addstr( 0, 0, msg )
        self.refresh( )

    def getch( self ):
        return self.stdscr.getch( )


screen = Screen( )
