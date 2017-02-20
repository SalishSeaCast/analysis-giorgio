#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:43:50 2017

@author: gsgarbi
"""
"""inputs:  bparam = st(d=18, m=7, y=2016)
            
"""


import os

import time

import numpy as np



from shutil import copyfile

import datetime as dt


inp = np.loadtxt("/home/gsgarbi/analysis-giorgio/notebooks/time_series/inp.txt", delimiter = ' ')

values = [int(x) for x in inp]
       
keys = ["year", "month", "day", "length"]

date_input = dict(zip(keys, values))

first_date = dt.datetime(
                 year = date_input["year"], 
                 month = date_input["month"], 
                 day = date_input["day"]
                 )



from createdirs import createdirs
from createnl import nl
from create_inpos import initp
from linkvel import link as link


def runariane(arianedir, resultsdir):
    
    start_time = time.time()


    os.chdir(arianedir)
    cmd = 'ariane'
    os.system(cmd) # returns the exit status
 
    
    src = arianedir + "/traj.txt"
    
    dst = resultsdir + "/traj.txt"
    
    copyfile(src, dst)
    
    os.chdir("/home/gsgarbi/analysis-giorgio/notebooks/time_series")
    
    print("the run took --- %s seconds ---" % (time.time() - start_time))
    
    print ("find results in ", dst)
    
    
    

def main(first_date, tlength):
    
    
    
    dirs = createdirs(first_date)
    

    
    arianedir = dirs["arianedir"]
    

    
    resultsdir = dirs["resultsdir"]
    

    

    nl(arianedir, tlength)
    
    initp(arianedir)
    
    link(tlength, first_date, arianedir)
    
    runariane(arianedir, resultsdir)
   
    



