import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    probRabbitReproduce = 1 - CURRENTRABBITPOP/ MAXRABBITPOP
    n = CURRENTRABBITPOP    
    for i in range(n):
        if random.random() < probRabbitReproduce:
            CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    probEatsRabbit = CURRENTRABBITPOP/MAXRABBITPOP
    n = CURRENTFOXPOP    
    for i in range(n):
        if CURRENTRABBITPOP > 10 and random.random() < probEatsRabbit:
            CURRENTRABBITPOP -= 1
            # give birth to new fox
            if random.random() < 1/3:
                CURRENTFOXPOP += 1
        else:
            #dies
            if CURRENTFOXPOP >=10 and random.random() < 9/10:
                CURRENTFOXPOP -= 1
            
                
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations, fox_populations = [], []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return(rabbit_populations, fox_populations)
    
    
# Assume MAXRABBITPOP = 1000, CURRENTRABBITPOP = 500, CURRENTFOXPOP = 30, numSteps = 200. 
# Plot two curves, one for the rabbit population and one for the fox population. 
# You won't be submitting the plots. They are for your own understanding.
simulation = runSimulation(200)
rabbits = simulation[0]
foxes = simulation[1]
pylab.plot(rabbits, 'g-')
pylab.plot(foxes, 'r-')

import numpy as np
coeffRabbits = np.polyfit(range(len(rabbits)), rabbits, 2)
coeffFoxes = np.polyfit(range(len(foxes)), foxes, 2)
pylab.plot(np.polyval(coeffRabbits, range(len(rabbits))), 'g-')
pylab.plot(np.polyval(coeffFoxes, range(len(foxes))), 'r-')