'''
@author: Devangini Patel
'''

class State:
    '''
    This class retrieves state information for social connection feature
    '''

    initialNode = ""
    
    def __init__(self,name ):
        self.name = name
    
    def setOrigin(self, origin):
        self.initialNode = origin

    def successorFunction(self, graph):
        """
        This is the successor function. It finds all the persons connected to the
        current person
        """
        return graph[self.name]
        
    #This method receive the goal entered by the user    
    def checkGoalState(self, goal):
        """
        This method checks whether the person is Jill.
        """ 
        #check if the person's name is the same person entered by the user as
        return self.name == goal
