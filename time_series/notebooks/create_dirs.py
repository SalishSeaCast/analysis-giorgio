
# coding: utf-8

# In[1]:

import os


import datetime as dt

months = ['', 'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']



# In[2]:
    

import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def createdirs (first_date, tlength, basedir = "/ocean/gsgarbi/analysis-giorgio/time_series/"):


  

    fdate = '{:%Y/%m/%d}'.format(first_date) + "/{} day(s)".format(tlength)

    arianedir = basedir + "arianefiles/" + fdate
    resultsdir = basedir + "results/" + fdate

    make_sure_path_exists(arianedir)

    make_sure_path_exists(resultsdir)
    
        
    print ("directories ", arianedir, resultsdir, "created")
    
    return {'arianedir': arianedir, 'resultsdir': resultsdir}
    
