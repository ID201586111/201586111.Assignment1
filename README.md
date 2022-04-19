# 201586111.github.io
 Assignment 1
 
Title: 
GEOG5003M Assignment 1, Online Portfolio

Description: 
The project contains two files for code; 'model.py' and 'agentframework.py' and one file containing raster data (in.txt)

The project creates a pop out window showing an environment with 10 random coordinates plotted (agents). 
These agents have are randomly moved 100 times, with each agent changing the environment. A text file is generated which lists the environment.

'agentframework.py' is an object oriented code which encapsulates the agents'properties and behaviour, as well as the 
agents' environment. This agent framework code is used by the main 'model.py'. In 'agentframework.py' the class 'Agent' is defined creating 
self.x and self.y coordinates- also defining getx/y, setx/y and delx/y. 
The code also defines 'move' which randomly moves x and y by 1 unit. This is carried out 100 times (but can be changedin main model). 
'agentframework.py' also containes code that defines 'eat' and 'share_with_neibours' these allow the agents to interact with the environment 
changing it as they move. Currently they 'eat' 10 units but this can also be changed in the main model.
Also contained in this code is defined 'distance_between' which uses pythagoras' theorem (c2 = a2 + b2), to find the distance 
between 2 points where the distance between to points is the hypotenuse (c2).
The Environment is also defined as 'get_data', this creates an empty list called environment and creates a new list for each row of 
values for the environment.

'model.py' is the main model and is the code that the user can run. The model has a timer which starts before the first line 
of code and ends after the last line of code for the model, printing 'time=' and the time the code took to proccess. 
Also before the code starts there is an option to set the random seed for reproducible resluts. The environment is set from 
'agentframework.py' next the user can control how many agents are plotted, how many iterations the random movement of agents
happen, and control the size of the neighbourhood.
Next using a loop, and the 'Agent' class from 'agentframework.py' the agents are created.
The using a nested loop and the 'move', 'eat' and 'share_with_neighbours' code from 'agentframework.py', the agents are moved, 
eatten and shared with neighbours.
Next is some code to find the distance between the agents, using pythagoras' theorem from 'agentframework.py'. The original code
has been left in to show how you would measure all agents agaisnt eachother. However, this has been commented out and after it 
there is code that optimises this code so that it iterates through each coordinate and does not reapeat i.e. measures point 1 to 
point 3 then measures point 3 to point 1. It also makes sure each coordinate is not measured against itself, returning zero units.
The model then uses the 'max' and 'min' functions to print the maximum distance between the agents and the minimum distance.
The environment is then printed in a seperate textfile using 'fileinput.input' which writes files.
Lastly using 'matplotlib' the environment is drawn over a grid (0,99 on x/y axis) and the agents are plotted over it.

The raster text file contains comma sparated variable data, each value being equivalent to a pixel in an image.

How to Run/Use Project:
Download the three files; 'model.py' and 'agentframework.py' and raster data (in.txt). 'model.py' will be the file where you can change
the inputs, 'agentframework.py' should not be edited unless you are changing the raster file for the environment.
If you have your own raster data in a txt file copy that to the same folder as the python files and call it 'in.txt' deleting the 'in.txt' 
file from the project folder. If you would like to keep the 'in.txt' file from the project folder and another raster you will need to edit
line 74 in 'agentframework.py' to 'f = open('YOUR RASTER TEXT FILE NAME HERE.txt', newline ='')'.

In the 'model.py' file you can edit row 28 to control the number of agents (coordinates) you want to show.
Edit row 30 to control the number of iterations the 'move' function will carry out.
Edit row 32 to control the number in the neighbourhood.

Also if you would like to set the random seed or turn it off edit the number in row 17.


Credits:
Student ID: 201586111
Using code from University of Leeds, MSc, GEOG5003M.

Testing:
The model was tested throughout using the timer to try and optimise the code and debugging to slove any issues.
