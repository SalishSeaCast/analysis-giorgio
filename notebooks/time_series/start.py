#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:43:50 2017

@author: gsgarbi
"""
"""inputs:  bparam = st(d=18, m=7, y=2016)
            
"""

import os, subprocess

import matplotlib

matplotlib.use('Agg')

from matplotlib import pyplot as plt
plt.ioff()



import numpy as np

import shutil

from shutil import copyfile

import datetime as dt

months = ['', 'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

inp = np.loadtxt("/home/gsgarbi/analysis-giorgio/notebooks/time_series/inp.txt", delimiter = ' ')

inp = [int(x) for x in inp]

import base

from base import start as st



def cycle(date = dt.datetime(year = 2016, month = 7, day = 18), tlength = 21):
    
    d = date.day
    m= date.month
    y = date.year
    
    bparam = st(d, m, y, n = tlength) #    return first_date, dirct, N, g, directory, resultsdir
    
    directory = bparam[4]
    
    first_date = bparam[0]
    
    resultsdir = bparam[5]
    
    
    
    N = bparam[2]
    
    from createnl import nl as nl
    nl(directory)
    
    from create_inpos import initp as initp
    initp(directory)
    
    from linkvel import link as link
    link(N, first_date, directory)
    
    
    
    def runariane(directory):
        os.chdir(directory)
        cmd = 'ariane --option --otheroption'
        os.system(cmd) # returns the exit status
    runariane(directory)
    
    os.chdir("/home/gsgarbi/analysis-giorgio/notebooks/time_series")
        
    
        
    from plotfinal import go as go
    go(directory, resultsdir, p = 17, f = first_date)
    

cycle(dt.datetime(year = inp[0], month = inp[1], day = inp[2]), tlength = inp[3])
#datei =  dt.datetime(year = 2016, month = 7, day = 19)
#
#tlength = 14
#
#howmanyinitialdays = 2
#    
#for i in range (howmanyinitialdays):
#cycle (datei + dt.timedelta(hours = 24), tlength)