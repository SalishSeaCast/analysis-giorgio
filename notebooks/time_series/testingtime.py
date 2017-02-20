
# coding: utf-8

# In[2]:

import subprocess

from subprocess import Popen

from subprocess import STDOUT, check_output




# In[ ]:




# In[3]:

proc = subprocess.Popen('ls')
try:
    outs, errs = proc.communicate(timeout=15)
except TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()


# In[4]:

#!/usr/bin/env python3

"""
Created on Wed Feb 15 11:31:31 2017

@author: gsgarbi
"""

import time, os

from shutil import copyfile

from timelimit import Command as Command

from createnl import nl as nl


def runexample(arianedir):
    
    
    start_time = time.time()
 

    os.chdir(arianedir)
    output = check_output('ariane', stderr=STDOUT, timeout= 5)
    
    print ()
    
    t = int(time.time() - start_time)
    
    return t
    



def runariane(arianedir, resultsdir, T):
    
    start_time = time.time()
    


    os.chdir(arianedir)
 

 
    
    src = arianedir + "/traj.txt"
    
    dst = resultsdir + "/traj.txt"
    
    copyfile(src, dst)
    
    
    print("the run took --- %s seconds ---" % (time.time() - start_time))
    print ("find results in ", dst)
    
    t = int(time.time() - start_time)
    
    return t


# In[5]:

#!/usr/bin/env python3

"""
Created on Thu Feb  9 21:43:50 2017

@author: gsgarbi
"""
"""inputs:  bparam = st(d=18, m=7, y=2016)
            
"""

import signal

#signal.pause()


import os

import time

import numpy as np


import signal
from contextlib import contextmanager

from runariane import runariane as runariane






from shutil import copyfile

import datetime as dt


inp = np.loadtxt("/home/gsgarbi/analysis-giorgio/notebooks/time_series/inp.txt", delimiter = ' ')

values = [int(x) for x in inp]
       
keys = ["year", "month", "day", "tlength", "length"]

date_input = dict(zip(keys, values))

first_date = dt.datetime(
                 year = date_input["year"], 
                 month = date_input["month"], 
                 day = date_input["day"]
                 )

tlength = date_input["tlength"] 

length = date_input["length"] 







from createdirs import createdirs
from createnl import nl
from create_inpos import initp
from linkvel import link as link
from catch_error import catch_error as catch_error

from runarianet import run_example as run_example

from runarianet import runariane as runarianet


    
    
T = 30 * tlength + 5 #estimated time
    


# In[6]:

# for i in range(length):
#     first_date = dt.datetime(
#              year = date_input["year"], 
#              month = date_input["month"], 
#              day = date_input["day"]
#              ) + dt.timedelta(hours = 24)
#     info = main(first_date, tlength)

#     infos.append(info)

#     print ("-------------------|--------------------")

#     for i in infos:

#         print ("xxxxxxxxxxxxxxx",
#                i,
#                "xxxxxxxxxxxxxxx")


# In[ ]:




# In[7]:

if __name__ == "__main__":
    runexample(arianedir="/home/gsgarbi/analysis-giorgio/arianefiles/2016/07/17")
    


# In[ ]:



