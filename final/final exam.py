# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:03:16 2017

@author: Vsevolod Loik
"""

# Problem 3
def oneTrial():
    balls = ['green','green','green','green','red','red','red','red']
    ballsChosen = []    
    for i in range(3):
        ball = random.choice(balls)
        ballsChosen.append(ball)
        balls.remove(ball)
    #print(ballsChosen)    
    if ballsChosen[0] == ballsChosen[1] and ballsChosen[1] == ballsChosen[2]:
        return True
    else:
        return False
       
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    countSameColor = 0
    for i in range(numTrials):
        if oneTrial():
            countSameColor += 1
    return countSameColor / numTrials
    
    
    
# Problem 4-1
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    if title == None:
        pass
    else:
        pylab.title(title)  
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longestRuns = []
    for i in range(numTrials): 
        rolls = []
        for j in range(numRolls):
            rolls.append(die.roll())
        longRun = 0
        count = 1
        if len(rolls) > 1:
            for n in range(len(rolls)-1):
                if rolls[n] == rolls[n+1]:
                    count += 1
                else:
                    count = 1
                if count > longRun:
                    longRun = count
        else: 
            longRun = 1
        longestRuns.append(longRun)
    expectedMean = getMeanAndStd(longestRuns)[0]
    makeHistogram(longestRuns, 10, 'Number of longest runs', 'Number of Trials')
    return expectedMean
    
       
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))




def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    result = [0]*len(choices)
    for i in choices:
        if i == total:
            result[i] = 1
        else:
            