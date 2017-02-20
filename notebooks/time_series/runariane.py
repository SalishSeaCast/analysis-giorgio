#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:31:31 2017

@author: gsgarbi
"""

import time, os

from shutil import copyfile

def runariane(arianedir, resultsdir):
    
    start_time = time.time()
    


    os.chdir(arianedir)
 
    
    src = arianedir + "/traj.txt"
    
    dst = resultsdir + "/traj.txt"
    
    copyfile(src, dst)
    
    
    print("the run took --- %s seconds ---" % (time.time() - start_time))
    print ("find results in ", dst)
    
    t = int(time.time() - start_time)
    
    return t