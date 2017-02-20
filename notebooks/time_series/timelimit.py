#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:12:13 2017

@author: gsgarbi
"""




import subprocess, threading
import os,signal
class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            print ('Thread started')
            self.process = subprocess.Popen(self.cmd, shell=True, preexec_fn=os.setsid)
            self.process.communicate()
            print ('Thread finished')

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print ('Terminating process')
            os.killpg(self.process.pid, signal.SIGTERM)
            thread.join()
        print (self.process.returncode)

#arianedir = "/home/gsgarbi/analysis-giorgio/arianefiles/2016/07/17"
#resultsdir = "/home/gsgarbi/analysis-giorgio/results/2016/07/17"
#
#os.chdir(arianedir)
#
#command = Command("ariane")
#command.run(timeout=10)
#
#print ("xxx")
#
#command.run(timeout=60)