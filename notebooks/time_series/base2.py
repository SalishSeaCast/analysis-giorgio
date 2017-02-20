
# coding: utf-8

# In[1]:

import os


import datetime as dt

months = ['', 'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']



# In[2]:

def createdirs (d, m, y, n, dircta = "/home/gsgarbi/analysis-giorgio/project4/"):


    first_date = dt.datetime(year = y, month = m, day = d)


    

    fdate = '{:%Y/%m/%d}'.format(first_date)

    arianedir = dircta + fdate
    resultsdir = "/home/gsgarbi/analysis-giorgio/" + "results" + fdate
    
    
    if not os.path.exists(arianedir):
        os.makedirs(resultsdir)
    if not os.path.exists(resultsdir):
        os.makedirs(resultsdir)
        
    fdict = {"first_date": first_date, "arianedir": arianedir, "resultsdir": resultsdir, "n": n}
        
    return fdict
    
