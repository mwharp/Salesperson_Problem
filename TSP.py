from itertools import permutations
import math
import numpy as np
import random

class GraphAlgorithms:
    #MAX HARPER 10/23/2020

    def __init__(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        self.dictionary ={}

        for line in graphFile:
            '''
            Get the two vertices and the cost
            '''
            (firstVertex, secondVertex, cost) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            # Update self.adjacencyList with a cost from city i to city j
            # Your code goes here:
            if firstVertex not in self.adjacencyList: #city not in thr
                self.dictionary = {}   #clear dictionary to introudce the new distances for firstVertex
            self.dictionary[secondVertex] = cost #getting the second vertex and the cost
            self.adjacencyList[firstVertex] = self.dictionary #adding to adjacencylist





        graphFile.close()

        self.vertices = list(set(self.vertices))
        print("y")
    
    def solve(self):
        min_cost = np.inf # initialize global min_cost as infinity
        min_path = [] # initialize min_path as empty
        visited = []
        currentDistance = 0
        totalDistance = 0
        flag = False
        randomCity = random.choice(self.vertices) #this gets a random city, this is where we will start
        randomIndex = self.vertices.index(randomCity)
        start = self.vertices.pop(randomIndex) # we don't need the starting city in the permutations
        
            
        # Your code goes here:
        p = permutations(self.vertices)
        for i in p: # the loop for permutations
            print(i)
            fromCity = start
            
            if flag == False:
                print('The salesman begins his journey')
                visited = []
            elif totalDistance < min_cost: # we got a new smallest distance
                    min_cost = totalDistance
                    min_path = visited
                    print("The min cost is: ", min_cost)
                    print("The min path is: ", min_path)
                    flag == False
                    visited = []
            visited = [] # clear visited for the next permutation
            totalDistance = 0 #reset
            check = 0 #reset
            visited.append(start) #start
            for toCity in i:
                check = check + 1
                if toCity in visited:
                    continue
                if fromCity == toCity:
                    continue
                currentDistance = self.adjacencyList[fromCity][toCity] # the distance between
                currentDistance = int(currentDistance)
                totalDistance = totalDistance + currentDistance #applying a new total distance
                visited.append(toCity) #this city has been visited
                fromCity = toCity #now we are in toCity, so reset the fromCity
                flag = True
                print("Visited: " , visited)
                if check == len(i): # if end of p was reached
                    toCity = start
                    currentDistance = self.adjacencyList[fromCity][toCity] # the distance between
                    currentDistance = int(currentDistance)
                    totalDistance = totalDistance + currentDistance #applying a new total distance
                    visited.append(toCity) #this city has been visited
                    fromCity = toCity 
                    flag = True
                    







        return min_cost, min_path

if __name__ == '__main__':
    
    g = GraphAlgorithms('vt.txt')
    print(g.solve())
    