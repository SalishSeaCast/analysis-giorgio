#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 23:18:41 2017

@author: gsgarbi
"""

from scipy.spatial import distance


import datetime as dt



class Traj:
    def __init__(self, traject, t0, deltat = 20):
        
        self.deltat = deltat
        
        self.traj = traject
    
        self.points = [(x[1], x[2]) for x in self.traj]

        self.particles = [x[0] for x in self.traj]
        
        self.t0 = t0
        
    def closest_p(self, p2):
        
        closest_p = self.points[distance.cdist([p2], self.points).argmin()]
        
        return closest_p
    
    def find_particle (self,point):

        when = self.points.index(point)

        P = self.particles[when]
        
        return P
    
    def time (self, point):
        return self.t0 + dt.timedelta(minutes= self.deltat * self.points.index(point))
    
    def timec (self, point):
        return self.t0 + dt.timedelta(minutes= self.deltat * self.points.index(self.closest_p(point)))
    
    def sub_traj(self, particle):
        T = [i for i in self.traj if i[0] == particle]
        print (T)
        b= Traj(traject = T, t0 = self.t0+dt.timedelta(minutes = particle*60), deltat = self.deltat)
        return b