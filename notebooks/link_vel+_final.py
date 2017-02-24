
# coding: utf-8

# In[32]:

import os, subprocess

import numpy as np

import shutil

from shutil import copyfile

import datetime as dt

months = ['', 'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

import base

# In[33]:

def link():


    for i in ("U", "V", "W"):
        linkfiles(vel = i)
    
    


# In[34]:

def smon (mon):
    months = ['', 'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    return months[mon]


# In[35]:

def sadd0(n):
    if n<10:
        return "0"+str(n)
    else:
        return str(n)


# In[36]:

def fd(date):
    dd = {
    "day": sadd0(date.day),
    "month": sadd0(date.month),
    "year": sadd0(date.year),
    "smonth": smon(date.month),
    "year2": sadd0(date.year)[-2:]
     }
    return dd


# In[39]:

def linkfiles (vel, n = base.N):
    
    date = base.first_date
    

    for i in range(1, n+1):
        

        f = fd(date)


        source = (f["day"], f["smonth"], f["month"], f["day"], f["month"], f["day"], vel, f["year2"], f["year"] )

        src = "/results/SalishSea/nowcast-green/{0}{1}{7}/SalishSea_1h_{8}{2}{3}_{8}{4}{5}_grid_{6}.nc".format(*source)

        fi = sadd0(i)
        dst = base.directory + "/SalishSea_{}_grid_{}.nc".format(fi, vel)


        if os.path.exists(dst):
            os.remove(dst)

        os.symlink(src, dst)

        date = date + dt.timedelta(hours = 24)


# In[40]:




# In[ ]:




# In[ ]:



