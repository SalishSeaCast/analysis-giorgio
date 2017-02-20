#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:36:29 2017

@author: gsgarbi
"""
import os

from runariane import runariane as runariane

from createnl import nl as nl

def catch_error(arianedir, resultsdir, n):
    
    
    nl(arianedir, n, 4)
    runariane (arianedir, resultsdir)
    if os.path.getsize(resultsdir + "/traj.txt") == 0:
        
        

        with open(resultsdir + "/error.txt", 'w') as file:
            file.write(" error :( ") 
    
        return True
    
    else:
        
        return False
    