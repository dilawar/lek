# -*- coding: utf-8 -*-
"""Rule.py: 

LEK rule.
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import re
import logging

black = 'black'
red = 'red'

class Rule( ):

    def __init__( self, expr ):
        self.expr = expr
        self.ite = None
        self.parse( self.expr )

    @classmethod
    def parse( self, expr ):
        pat = re.compile( r'(?P<if>.+?)\?(?P<then>.+?):(?P<else>.+)')
        m = pat.match( expr )
        if not m:
            logging.warning( "Invalid rule %s" % expr )
            return None
        return m.groupdict( )

    @classmethod
    def ite_to_expr( self, ite ):
        return '{then} if {if} else {else}'.format( **ite )

    def eval( self, prev, cur ):
        expr = self.expr
        cards = [ prev, cur ]
        colors = [ x.color for x in cards ]
        expr = expr.replace( 'PREV', 'prev' )
        expr = expr.replace( 'CUR', 'cur' )
        ite = self.parse( expr )
        expr = self.ite_to_expr( ite )
        val = eval( expr )
        logging.debug( prev, cur, expr, val )
        return val

    def __str__( self ):
        return self.expr
