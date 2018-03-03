#!/usr/bin/env python

"""lek.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import logging
from globals import *


def play( args ):
    print( [ str(x) for x in players_ ] )
    print( grid_ )


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
