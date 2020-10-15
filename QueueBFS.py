'''
@author: Devangini Patel
Modified and adapted by: Victor Chaparro
'''

from Node import Node
from State import State
from collections import deque
from GraphData import *
from Treeplot import TreePlot


def main():
        
    #Reading and asigning initial parameters
    print("Provide the name of the student to connect")
    originNode = input()
    
    graph = connections
    #calling BFS Function passing 3 parameters
    if originNode in graph:
        print("Provide the name of the target student")
        goalNode = input()
        if goalNode in graph:
            BFS_Victor(graph, originNode, goalNode)
        else:
            print("Target student not found in the student list")
    else:
        print("Student to connect not found int the student list")
    


def BFS_Victor(graph, originNode, goalNode):
    """
    This function performs BFS search using a queue
    """
    #create queue
    queue = deque([]) 
    #since it is a graph, we create visited list
    visited = [] 
    #create root node
    initialState = State(originNode)
    initialState.setOrigin(originNode)
 

    root = Node(initialState)
    #add to queue and visited list
    queue.append(root)    
    visited.append(root.state.name)
    # check if there is something in queue to dequeue
    while len(queue) > 0:
        
        #get first item in queue
        currentNode = queue.popleft()
        
        print (("-- dequeue --"), currentNode.state.name)
        
        #check if this is goal state
        if currentNode.state.checkGoalState(goalNode):
            print ("reached goal state")
            #print the path
            print ("----------------------")
            print ("Path")
            currentNode.printPath()
            #Defining if the goal is reached
            reachedGoal = True
            break           
        #get the child nodes 
        childStates = currentNode.state.successorFunction(graph)
        for childState in childStates:
            
            childNode = Node(State(childState))
            
            #check if node is not visited
            if childNode.state.name not in visited:
                
                #add this node to visited nodes
                visited.append(childNode.state.name)
                
                
                #add to tree and queue
                currentNode.addChild(childNode)
                queue.append(childNode)
            treeplot = TreePlot()
            treeplot.generateDiagram(root, currentNode) 
           
    treeplot = TreePlot()
    treeplot.generateDiagram(root, currentNode)                     
    #print tree
    print ("----------------------")
    print ("Tree")
    root.printTree()
    if reachedGoal != True:
        print ("No connection was found between ", originNode," and", goalNode)
    
if __name__ == "__main__":
    main()