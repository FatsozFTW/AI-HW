from random import random,randint # random() generates a uniform random number in [0.0, 1.0]
from math import ceil

EVALS = 0

n = 8
#intial board
randomSuccIndex = 0
def initial():
    grid =[]
    for i in range(n):
        grid.append(randint(1,8))
    return grid


def metrop(dE, T):
  r=random()
  return (dE>0) or (r<exp(dE/T))

# returns 1 if queens q1 and q2 are attacking each other, 0 o.w.
def attacking(q1col, q1row, q2col, q2row):
  if q1col==q2col:
    return 1  # same column
  if q1row==q2row:
    return 1  # same row
  coldiff=q1col-q2col
  rowdiff=q1row-q2row
  if abs(coldiff)==abs(rowdiff):
    return 1  # same diagonal
  return 0 

# evaluates the fitness of an encoding, defined as the number of
# non-attacking pairs of queens (28 - number of attacking pairs)
#
# the global variable EVALS keeps track of the number of times called
def fitness(encoding):
  global EVALS
  EVALS += 1
  E = 28
  for i in range(1,8):
    for j in range(i+1,9):
      E -= attacking(i, encoding[i-1], j, encoding[j-1])
  return E

# the following is useful in a variety of algorithms
# returns the nth successor of an encoding
def getsuccessor(init, n, succ):
  n -= 1
  quotient, remainder = divmod(n,7) 
  newrow=init[quotient]+remainder+1
  if newrow>8:
    newrow -= 8
  for j in range(8):
    if j==quotient:
      succ[j]=newrow
    else:
      succ[j]=init[j]


def hillclimb(grid):
    current = grid #intial
    neighbor = current[:]
    bestE = 0
    while True:
        for i in range(1, 57):
            getsuccessor(current, i, neighbor)
            f = fitness(neighbor)
            if f > bestE or (f==bestE and random() < 0.001):
                bestE = f
                
            if bestE == 28:
                print("Solution: ", neighbor)
                print("EVALS: ", EVALS)
                return neighbor
        if fitness(neighbor) <= fitness(current):
            randomSuccIndex = int(ceil(random()*56))
            getsuccessor(current, randomSuccIndex, neighbor)

        current = neighbor
    
#Run here
average = 0
for i in range(100):
    EVALS = 0
    print("iter", i)
    hillclimb(initial())
    average += EVALS

print("The average: ", average/100)
