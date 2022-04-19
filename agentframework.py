# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:58:19 2022

@author: dan-8
"""

import random
import csv

#Make Agents
class Agent():
    def __init__(self, environment, agents):
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property")
                 
    
    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value
    def dely(self):
        del self._y
    y = property(gety, sety, dely, "I'm the 'y' property")

#Move agents
    def move(self):
        if random.random() <0.5:
            self._y = (self._y + 1) %100
        else:
            self._y = (self._y - 1) %100
        if random.random() <0.5:
            self._x = (self._x + 1) %100
        else:
            self._x = (self._x - 1) %100
            
          
#eat self
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
#neighbours      
    def share_with_neighbours(self, neighbourhood):
         for agent in self.agents:
             dist = self.distance_between(agent)
             if dist <= neighbourhood and dist != 0:
                 sum = self.store + agent.store
                 ave = sum /2
                 self.store = ave
                 agent.store = ave
             else:
                ave = 0
                 #print("sharing " + str(dist) + " " + str(ave))
#Distance between points
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 

#Environment 
def get_data():
    #Add this data, to 2d list
    environment = []    #Make empty list before any processing done
    f = open('in.txt', newline ='')
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist =[]     #Make new list before each row is processed
        for value in row:
            rowlist.append(value) #Append the values to the rowlist
        environment.append(rowlist)
    f.close()
    return environment