

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 12:58:01 2022

@author: dan-8
"""

import random
import matplotlib.pyplot
import matplotlib.animation
import time
import agentframeworkanimated
import csv

# Set the random seed for reproducible results
random.seed(0)
#random.seed(1)

#start the clock
start = time.process_time()

environment = agentframeworkanimated.get_data()


#Control How many agents we have
num_of_agents = 10
#control how many iterations we have
num_of_iterations = 10
#control neighbourhood
neighbourhood = 20

#create empty list for agents, to add coords to.
agents =[]

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 100, 100])

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframeworkanimated.Agent(environment, agents))

# Move the agents, eat agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

def update(frame_number):
    
    fig.clear()   

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

#Distance between agents        
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = agentframeworkanimated.Agent.distance_between\
        (agents_row_a, agents_row_b)
        #print (distance)
        
#Optimise so no repeats
#iterate through each coordinate
for agents_row_a in agents:
    for agents_row_b in agents:
        if agents_row_a != agents_row_b and agents_row_a.getx()\
            < agents_row_b.getx():
            distance = agentframeworkanimated.Agent.distance_between\
            (agents_row_a, agents_row_b)
            distance_list= []
            distance_list.append(distance)
            #print("Distance:", str(distance))
            
        
#Distances
distances = []
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = agentframeworkanimated.Agent.distance_between(agents_row_a,\
                                                         agents_row_b)
        distances.append(distance)


#Max Min distance
maxd = agentframeworkanimated.Agent.distance_between(agents[0], agents[1])
mind = agentframeworkanimated.Agent.distance_between(agents[0], agents[1])
distances = []
for i in range(0, num_of_agents, 1):
    for j in range(i+1, num_of_agents, 1):
    #for j in range(0, num_of_agents, 1):
        if (i < j):
        #if (i != j):
            #print(i, j)
            distance = agentframeworkanimated.Agent.distance_between\
            (agents[i], agents[j])
            maxd = max(maxd, distance)
            mind = min(mind, distance)
print("maxd", maxd)       
print("mind", mind)       
        
#Write Environment as text file
write_environment= open("Environment.txt", "w", newline='')
writer  =csv.writer(write_environment, delimiter= ",")
for row in environment:
    writer.writerow(row)
write_environment.close()

#Write Agents as text file
#write_agents= open("Agent_Values.txt", "a")
#for row in range(num_of_agents):
#    write_agents.write(str(agentframeworkanimated.Agent.agents, ",")
#write_agents.write("\n")
#write_agents.close()


#plot on graph
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
#end timer
end = time.process_time()

print ("time= " +str(end - start))