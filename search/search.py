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
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    frontier = util.PriorityQueue()
    frontier.push((start, [], 0), 0)   # (state, actions, g)
    bestCost = {start: 0}

    while not frontier.isEmpty():
        state, actions, g = frontier.pop()

        # Skip outdated (more expensive) copy
        if g != bestCost.get(state, float("inf")):
            continue

        if problem.isGoalState(state):
            return actions

        for succ, action, stepCost in problem.getSuccessors(state):
            newG = g + stepCost
            if newG < bestCost.get(succ, float("inf")):
                bestCost[succ] = newG
                frontier.push((succ, actions + [action], newG), newG)

    return []

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    node_list = util.PriorityQueue()
    node_list.push((start, []), heuristic(start, problem))
    #keep a list of visted nodes to avoid cycles
    visited = {}
    while not node_list.isEmpty():
        node, path = node_list.pop() # Pop the next node from the priority queue
        g = problem.getCostOfActions(path) # Get the cost of the path to the current node
        if node in visited and visited[node] <= g:
            continue
        visited[node] = g # Mark the current node as visited with its cost
        if problem.isGoalState(node):
            return path # Return the path to the goal if found
        for successor, action, stepCost in problem.getSuccessors(node):
            new_path = path + [action] # Create a new path by adding the action to the current path
            new_g = g + stepCost # Calculate the new cost to reach the successor
            new_f = new_g + heuristic(successor, problem) # Calculate the f(n) value for the successor
            node_list.push((successor, new_path), new_f) # Push the successor onto the priority queue with its f(n) value
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
