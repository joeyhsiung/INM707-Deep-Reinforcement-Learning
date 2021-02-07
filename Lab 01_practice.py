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
# In[]
dungeon = Dungeon(10)
dungeon.reset()

print(dungeon.position_agent)
dungeon.display()
obs, reward, done = dungeon.step( ... )

print(dungeon.position_agent)
# In[]
import numpy as np
class Dungeon:
    def __init__(self, N):
        self.dungeon = np.zeros((N, N))

    def abc(self,b): 
        b += 10
        return b
                
a = Dungeon(5).dungeon
a = 5**2
# In[]
from random import randrange
N = 6
dung_array = np.zeros((N,N))
        
        # Making dungeon borders = 1
dung_array[:,[0,-1]] = dung_array[[0,-1]] = 1
obs_idx_x = np.random.randint(1, dung_array.shape[0]-1, N)

rnd_x = randrange(1,N-1)




a = (None,None)
a = np.array([3,4])


actions = {'up':(0,1),'down':(0,-1),'left':(-1,0),'right':(1,0)}
direction = np.random.choice(list(actions.keys()))
action = {'ac':actions[direction]}

rewards = {1:-5,2:-20,0:-1,3:(N**2)}




action = 'left'
actions = {'up':(0,1),'down':(0,-1),'left':(-1,0),'right':(1,0)}
X = actions[action][0]
Y = actions[action][1]
dung_array[:,[0,-1]]
