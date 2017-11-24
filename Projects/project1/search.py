# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    initialState =  problem.getStartState()
    actionList = []
    closed = set()
    fringe = Stack()
    fringe.push((initialState,actionList))
    while fringe.isEmpty() == False:
        node = fringe.pop()
        state = node[0]
        action = node[1]

        if problem.isGoalState(state) == True:
            return action
        if state not in closed:
            closed.add(state)
            children = problem.getSuccessors(state)
            for child in children:
                newActionList = action[:]
                newActionList.append(child[1])
                fringe.push((child[0],newActionList))
    return



def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    from util import Queue

    initialState =  problem.getStartState()
    actionList = []
    closed = set()
    fringe = Queue()
    fringe.push((initialState,actionList))
    while fringe.isEmpty() == False:
        node = fringe.pop()
        state = node[0]
        action = node[1]

        if problem.isGoalState(state) == True:
            return action
        if state not in closed:
            closed.add(state)
            children = problem.getSuccessors(state)
            for child in children:
                newActionList = action[:]
                newActionList.append(child[1])
                fringe.push((child[0],newActionList))
    return

def uniformCostSearch(problem):
    from util import PriorityQueue

    fringe = PriorityQueue()
    initialActionList = []
    initialState = problem.getStartState()
    fringe.push((initialState, initialActionList, 0), 0)

    closed = set()

    while not fringe.isEmpty():
        state = fringe.pop()
        currentState = state[0]
        actionList = state[1]
        cost = state[2]

        if problem.isGoalState(currentState):
            return actionList

        if currentState not in closed:
            closed.add(currentState)
            successors = problem.getSuccessors(currentState)
            for successor in successors:
                newState = successor[0]
                newAction = successor[1]
                newCost = cost + successor[2]
                newActionList = actionList[:]
                newActionList.append(newAction)
                fringe.push((newState, newActionList, newCost), newCost)
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    from util import PriorityQueue

    fringe = PriorityQueue()
    initialActionList = []
    initialState = problem.getStartState()
    currentCost = 0
    totalCost = heuristic(initialState, problem)
    fringe.push((initialState, initialActionList, currentCost, totalCost), totalCost)

    closed = set()

    while not fringe.isEmpty():
        state = fringe.pop()
        currentState = state[0]
        actionList = state[1]
        cost = state[2]

        if problem.isGoalState(currentState):
            return actionList

        if currentState not in closed:
            closed.add(currentState)
            successors = problem.getSuccessors(currentState)
            for successor in successors:
                newState = successor[0]
                newAction = successor[1]
                newCost = cost + successor[2]
                newTotalCost = newCost + heuristic(newState, problem)
                newActionList = actionList[:]
                newActionList.append(newAction)
                fringe.push((newState, newActionList, newCost, newTotalCost), newTotalCost)
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
