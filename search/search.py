# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    visited = set()
    visited.add(problem.getStartState())


    while not stack.isEmpty():
        vertex, path = stack.pop()   
        if problem.isGoalState(vertex):
            return path
        visited.add(vertex)
        for next_node in problem.getSuccessors(vertex):
            state = next_node[0]
            direction = next_node[1]
            if state not in visited:
                stack.push((state, path + [direction]))        
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    bfs_queue = util.Queue()
    visited = set()
    bfs_queue.push((problem.getStartState(), []))
    visited.add( problem.getStartState() )

    while bfs_queue.isEmpty() == 0:
        vertex, path = bfs_queue.pop()
        if problem.isGoalState(vertex):
            return path
        for next in problem.getSuccessors(vertex):
            state = next[0]
            direction = next[1]
            if state not in visited:
                bfs_queue.push( (state, path + [direction]) )
                visited.add(state)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    if problem.isGoalState(start): 
        return (start, [])

    frontier = util.PriorityQueue()
    visited = set()
    
    frontier.update((start, []), 0)
    
    while not frontier.isEmpty():
        vertex, path = frontier.pop()
       
        if problem.isGoalState(vertex):
            return path
        if vertex not in visited:
            visited.add(vertex)
            for next_node in problem.getSuccessors(vertex):
                state = next_node[0]
                direction = next_node[1]
                if state not in visited:
                    frontier.update((state, path + [direction]), next_node[2])
                    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStar_reArrange(astar_queue, item, priority):
    import heapq
    for index, (p, c, i) in enumerate(astar_queue.heap):

        if i[0] == item[0]:
            if p <= priority:
                break
            del astar_queue.heap[index]
            astar_queue.heap.append((priority, c, item))
            heapq.heapify(astar_queue.heap)
            break
    else:
        astar_queue.push(item, priority)


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    astar_queue = util.PriorityQueue()
    visited = []
    astar_queue.push((problem.getStartState(), []), heuristic(problem.getStartState(), problem))
    visited.append(problem.getStartState())

    while astar_queue.isEmpty() == 0:
        state, actions = astar_queue.pop()
        # print state
        if problem.isGoalState(state):
            # print 'Find Goal'
            return actions

        if state not in visited:
            visited.append(state)

        for next_node in problem.getSuccessors(state):
            node_state = next_node[0]
            node_direction = next_node[1]
            if node_state not in visited:
                aStar_reArrange(astar_queue, (node_state, actions + [node_direction]),
                                problem.getCostOfActions(actions + [node_direction]) + heuristic(node_state, problem))

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


