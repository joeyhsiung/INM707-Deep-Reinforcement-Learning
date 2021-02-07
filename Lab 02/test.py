# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:10:44 2021

@author: junru
"""
import numpy as np
N=10 
state_transition_matrix = np.zeros( (N*N, 4, N*N) )
policy = np.ones((N,N,4))/4

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print('My name is %s...' % self.name)
        print('My friend is %s...' % friend)
p = Person('Tom','male')

p('Tony')