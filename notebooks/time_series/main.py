import time
import datetime as dt
from shutil import copyfile

import numpy as np

from createdirs import createdirs
from createnl import namelist
from create_inpos import initp
from linkvel import link as link
from handle_error import check_error


inp = np.loadtxt("/ocean/gsgarbi/analysis-giorgio/notebooks/time_series/inptest.txt", delimiter = ' ')

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


    
    

def main(first_date, tlength):
    '''comments'''
    
    
    fdate = '{:%Y/%m/%d}'.format(first_date)
    
    dirs = createdirs(first_date, tlength)
    
    arianedir = dirs["arianedir"]
    
    resultsdir = dirs["resultsdir"]
    
    #errordir = dirs["errordir"]
       

    namelist(arianedir, tlength)
    
    initp(arianedir)
    
    link(tlength, first_date, arianedir)

    

    #copy basic files
    src = arianedir + "/namelist"
    dst = resultsdir + "/namelist"
    copyfile(src, dst)

    
    src = arianedir + "/initial_positions.txt"
    dst = resultsdir + "/initial_positions.txt"
    copyfile(src, dst)
    
    
    #run ariane
    error, log = check_error(arianedir, resultsdir)
    

    #copy results
    src = arianedir + "/traj.txt"
    dst = resultsdir + "/traj_{}.txt".format(tlength)   
    copyfile(src, dst)
    
    
    
    
        
    if error:

        ferrormsg = {"day" : first_date, "executed": dt.datetime.now()}
        errormsg = "Error encountered for file {day}, on {executed}"
        "with initial_positions.txt and namelist files in this folder,"
        "(Error provided by the author, not Ariane.) "
        
        print (errormsg.format(**ferrormsg))
        
        errorfilename = "/error.txt"
        
        
        
        time.sleep(5)
        

        
    if not error:
        
        ferrormsg = {"day" : first_date, "executed": dt.datetime.now()}
        errormsg = "No error encountered for file {day}, on {executed}"
        "with initial_positions.txt and namelist files in this folder,"
        "(Error provided by the author, not Ariane.) ".format(**ferrormsg)
        
        errorfilename = "/no error.txt"
        
        print (errormsg.format(**ferrormsg))
        
        time.sleep(2)
        
    with open(resultsdir + errorfilename, 'w') as file:
        file.write(errormsg.format(**ferrormsg)) 

    with open(resultsdir + "/log.txt", 'w') as file:
        file.write(log) 

    return (fdate, "error: {}".format(error))
    
    
    

    


    
def runlength (length):
          
    infos = []
    for i in range(length):
        first_date = dt.datetime(
                 year = date_input["year"], 
                 month = date_input["month"], 
                 day = date_input["day"] + i
                 )
        info = main(first_date, tlength)
        
        infos.append(info)
 
        print ("---------------------------------------")
    
    for i in infos:
        
        print ("xxxxxxxxxxxxxxx",
               i,
               "xxxxxxxxxxxxxxx\n")
        
    time.sleep(3)
        

     
if __name__ == "__main__":
    runlength(length)
        




