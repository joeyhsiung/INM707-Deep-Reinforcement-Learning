# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:19:28 2021

@author: junru
"""
import numpy as np
import matplotlib.pyplot as plt

class Dungeon:
    
    def __init__(self, N):
        
        # Numpy array that holds the information about the environment
        obstacles,lava = N/2,N/2
        self.dungeon = np.zeros(N, N)
        
        # position of the agent and exit will be decided by resetting the environment.
        self.position_agent = (0,0)
        self.position_exit = (N,N)
        
        # run time
        self.time_elapsed = 0
        self.time_limit = N*N
        
    def step(self, action):
        
        # action is 'up', 'down', 'left', or 'right'
        
        # modify the position of the agent
        
        # calculate total reward
        
        # calculate observations
        
        # update time
        self.time_limit -= 1
        # verify termination condition
        done =...
        
        return observations, reward, done
    
    def display(self):
        
        # prints the environment
        ...
        
    def reset(self):
        """
        This function resets the environment to its original state (time = 0).
        Then it places the agent and exit at new random locations.
        
        It is common practice to return the observations, 
        so that the agent can decide on the first action right after the resetting of the environment.
        
        """
        
        # position of the agent is a numpy array
        self.position_agent = ...
        
        # position of the exit is a numpy array
        self.position_exit = ...
        
        # Calculate observations
    
        return observations
