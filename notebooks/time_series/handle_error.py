import subprocess
import os
import signal


def handler(signum, frame):
    raise OSError


def check_error(arianedir, resultsdir):
     
    
    
    
    
    
    
    os.chdir(arianedir)
    ar = subprocess.Popen('/ocean/gsgarbi/MEOPAR/Ariane/bin/ariane', stdout=subprocess.PIPE)
    
    reader = ar.stdout
    
    
    log = ''

    while ar.poll() is None:
        
    

        signal.signal(signal.SIGALRM, handler)
    
    
        try:
            signal.alarm(3)
            

            # This reader.readline() may hang indefinitely     
            w = reader.readline().decode('ascii')
            


            print (w)
            
            log = log + w
            
            signal.alarm(0) #deactivate the alarm
            
        except OSError:
            
            log = log + "\n error!!!"

            ar.kill()
            return True, log
        

        
    return False, log
        
#if __name__ == "__main__":
#    #check_error(ex_dir1)
#    ex_dir = ex_dir2
#    time.sleep(2)
#    
#    
#    
#    
#    
#    if check_error(ex_dir):
#        print ("Found an error for the Ariane run in {}. Moved to the next file".format(ex_dir))
#    else:
#        print ("no error")

