#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:09:24 2017

@author: gsgarbi
"""

from traj import Traj

import matplotlib.pyplot as plt
import numpy as np
import matplotlib. animation as animation

def _update_plot (i, fig, scat):
    scat.set_offsets(i+50)
    print ('Frames: {}'.format(i))
    
    return scat,

fig = plt.figure()

x = 0
y = 0

limx = [-124.5,-122.5]

limy = [48.7,49.5]

ax = fig.add_subplot(111)
ax.grid (True, linestyle = '-', color = '0.75')
ax.set_xlim(limx)
ax.set_ylim(limy)

scat = plt.scatter (x,y, c=x)
scat.set_alpha (0.8)

anim = animation.FuncAnimation (fig, _update_plot, fargs= (fig, scat),
                                frames = 100, interval = 100)


