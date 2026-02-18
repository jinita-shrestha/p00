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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    frontier = util.Stack()
    frontier.push((start, []))   # (state, actions/path)
    visited = set()

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                frontier.push((successor, actions + [action]))

    return []
    

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    frontier = util.Queue()
    frontier.push((start, []))
    visited = set([start])

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                visited.add(successor)
                frontier.push((successor, actions + [action]))

    return []




def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    f_cost = util.PriorityQueue()
    f_cost.push((start, [], 0), heuristic(start, problem))
    #keep a list of visted nodes to avoid cycles
    visited = []
    while not f_cost.isEmpty():
        node, path, g_cost = f_cost.pop() # Pop the next node from the priority queue
        if problem.isGoalState(node): # Check if goal state is reached
            return path
        if node not in visited: # If the node has not been visited, add it to the visited list
            visited.append(node)
            for successor, path, step_cost in problem.getSuccessors(node): # Iterate through the successors of the current node
                new_g_cost = g_cost + step_cost
                new_f_cost = new_g_cost + heuristic(successor, problem)
                f_cost.push((successor, path + [path], new_g_cost), new_f_cost)
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
