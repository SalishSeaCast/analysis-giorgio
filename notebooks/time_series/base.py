
# coding: utf-8

# In[1]:

import os, subprocess

import numpy as np

import shutil

from shutil import copyfile

import datetime as dt

months = ['', 'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']



# In[2]:

def start (d, m, y, n, dircta = "/home/gsgarbi/analysis-giorgio/project4/"):


    first_date = dt.datetime(year = y, month = m, day = d)
    dirct = dircta
    N = n
    

    fdate = '{:%Y/%m/%d}'.format(first_date)

    directory = dirct + fdate
    resultsdir = "/home/gsgarbi/analysis-giorgio/" + "results" + fdate
    
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(resultsdir):
        os.makedirs(resultsdir)
        
    fdict = {"first_date": first_date, "directory": directory, "resultsdir": resultsdir, "N": N}
        
    return fdict
    
    


# In[3]:

def smon (mon):
    months = ['', 'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    return months[mon]


# In[4]:

def sadd0(n):
    if n<10:
        return "0"+str(n)
    else:
        return str(n)


# In[5]:

def fd(date):
    dd = {
    "day": sadd0(date.day),
    "month": sadd0(date.month),
    "year": sadd0(date.year),
    "smonth": smon(date.month),
    "year2": sadd0(date.year)[-2:]
     }
    return dd
    
