#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Sasha Lukas"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    pass


def main(args):
    """Implementation of echo"""
    result = "Dummy Result"
    return result


if __name__ == '__main__':
    main(sys.argv[1:])
