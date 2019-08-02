#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:35:52 2019

@author: sflippl
"""

import sys

def informative_exception(e, msg):
    type(e)(str(e) + msg).with_traceback(sys.exc_info()[2])