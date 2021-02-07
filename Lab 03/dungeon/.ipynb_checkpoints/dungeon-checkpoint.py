import numpy as np

class Dungeon:
    
    def __init__(self, N):
        
        # Numpy array that holds the information about the environment
        self.dungeon = np.zeros((N, N), dtype = np.int8)
        self.size = N
        
        # Borders are obstacles
        self.dungeon[0, :] = 1
        self.dungeon[-1, :] = 1
        self.dungeon[:, 0] = 1
        self.dungeon[:, -1] = 1
        
        # Pick N/2 random coordinates for the obstacles
        empty_coord = self.get_empty_cells( int(self.size/2) )
        self.dungeon[empty_coord[0], empty_coord[1]] = 1
        
        # Pick N/2 random coordinates for the lava
        empty_coord = self.get_empty_cells( int(self.size/2) )
        self.dungeon[empty_coord[0], empty_coord[1]] = 2
                
        # initial position of the agent will be decided by resetting the environment.
        self.position_agent = None
        
        # run time
        self.time_elapsed = 0
        self.time_limit = self.size**2
        
        # display help
        self.dict_map_display={ 0:'.',
                                1:'X',
                                2:'L',
                                3:'E',
                                4:'A'}
        
        # position of the exit
        self.position_exit = self.get_empty_cells(1)
        self.dungeon[self.position_exit[0], self.position_exit[1]] = 3
    
    def get_empty_cells(self, n_cells):
        empty_cells_coord = np.where( self.dungeon == 0 )
        selected_indices = np.random.choice( np.arange(len(empty_cells_coord[0])), n_cells )
        selected_coordinates = empty_cells_coord[0][selected_indices], empty_cells_coord[1][selected_indices]
        
        if n_cells == 1:
            return np.asarray(selected_coordinates).reshape(2,)
        
        return selected_coordinates
        
    
    def step(self, action):
        
        # At every timestep, the agent receives a negative reward
        reward = -1
        bump = False
        
        # action is 'up', 'down', 'left', or 'right'
        if action == 'up':
            next_position = np.array( (self.position_agent[0] - 1, self.position_agent[1] ) )
        if action == 'down':
            next_position = np.array( (self.position_agent[0] + 1, self.position_agent[1] ) )
        if action == 'left':
            next_position = np.array( (self.position_agent[0] , self.position_agent[1] - 1 ) )
        if action == 'right':
            next_position = np.array( (self.position_agent[0] , self.position_agent[1] + 1) )
        
        # If the agent bumps into a wall, it doesn't move
        if self.dungeon[next_position[0], next_position[1]] == 1:
            bump = True
        else:
            self.position_agent = next_position
        
        # calculate reward
        current_cell_type = self.dungeon[self.position_agent[0], self.position_agent[1]]
        if current_cell_type == 2:
            reward -= 20
        
        if current_cell_type == 3:
            reward += self.size**2
            
        if bump:
            reward -= 5
        
        # calculate observations
        observations = self.calculate_observations()
        
        # update time
        self.time_elapsed += 1
        
        # verify termination condition
        done = False
        
        if self.time_elapsed == self.time_limit:
            done = True
        
        if (self.position_agent == self.position_exit).all():
            done = True
            
        return observations, reward, done, bump

    def display(self):
        
        envir_with_agent = self.dungeon.copy()
        envir_with_agent[self.position_agent[0], self.position_agent[1]] = 4
        
        full_repr = ""

        for r in range(self.size):
            
            line = ""
            
            for c in range(self.size):

                string_repr = self.dict_map_display[ envir_with_agent[r,c] ]
                
                line += "{0:2}".format(string_repr)

            full_repr += line + "\n"

        print(full_repr)

        
    def calculate_observations(self):
        
        relative_coordinates = self.position_exit - self.position_agent
                
        surroundings = self.dungeon[ self.position_agent[0] -1: self.position_agent[0] +2,
                                     self.position_agent[1] -1: self.position_agent[1] +2]
        
        obs = {'relative_coordinates':relative_coordinates,
               'surroundings': surroundings}
        
        return obs
        
    def reset(self):
        """
        This function resets the environment to its original state (time = 0).
        Then it places the agent and exit at new random locations.
        
        It is common practice to return the observations, 
        so that the agent can decide on the first action right after the resetting of the environment.
        
        """
        self.time_elapsed = 0
        
        # position of the agent is a numpy array
        self.position_agent = np.asarray(self.get_empty_cells(1))
        
        # Calculate observations
        observations = self.calculate_observations()
        
        return observations
    
    
def run_single_exp(envir, policy):
    
    state = envir.reset()
    done = False
    
    total_reward = 0
    
    while not done:
        
        action = policy(state)
        state, reward, done = envir.step(action)
        
        total_reward += reward
    
    return total_reward


def run_experiments(envir, policy, number_exp):
    
    all_rewards = []
    
    for n in range(number_exp):
        
        final_reward = run_single_exp(envir, policy)
        all_rewards.append(final_reward)
    
    max_reward = max(all_rewards)
    mean_reward = np.mean(all_rewards)
    var_reward = np.std(all_rewards)
    
    return all_rewards, max_reward, mean_reward, var_reward