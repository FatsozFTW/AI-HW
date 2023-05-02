from random import random,randint # random() generates a uniform random number in [0.0, 1.0]
from math import ceil
from copy import deepcopy

EVALS = 0

cycle = 1
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
  
def col_chooser(my_col):
  if my_col == 1:
    return(1,7)
  elif my_col == 2:
    return(8,14)
  elif my_col == 3:
    return(15,21)
  elif my_col == 4:
    return(22,28)
  elif my_col == 5:
    return(29,35)
  elif my_col == 6:
    return(36,42)
  elif my_col == 7:
    return(43,49)
  else:
    return(50,57)

def random_col():
  return(col_chooser(randint(1,8)))

def cyclic_col():
  global cycle
  if cycle == 8:
    cycle = 1
  else:
    cycle+=1
  return(col_chooser(cycle))


def min_conflict_rand(grid, max_steps):
    current = grid #intial
    neighbor = deepcopy(current)
    bestE = 0
    for i in range(max_steps):
        var_col = random_col()
        for i in range(var_col[0], var_col[1]):
            getsuccessor(deepcopy(current), i, neighbor)
            f = fitness(neighbor)
            curr = fitness(current)
            #print(curr, f)
            if f > curr:
                bestE = f
                current = deepcopy(neighbor)
                
            if bestE == 28:
                print("Solution: ", neighbor)
                print("EVALS: ", EVALS)
                return "passed"

        
    return "failed"

def min_conflict(grid, max_steps):
    current = grid #intial
    neighbor = current[:]
    bestE = 0
    for i in range(max_steps):
        var_col = cyclic_col()
        for i in range(var_col[0], var_col[1]):
            getsuccessor(deepcopy(current), i, neighbor)
            f = fitness(neighbor)
            curr = fitness(current)
            #print(curr, f)
            if f > curr:
                bestE = f
                current = deepcopy(neighbor)
                
            if bestE == 28:
                print("Solution: ", neighbor)
                print("EVALS: ", EVALS)
                return "passed"
    return "failed"

#Run here


average_rand = 0
num_pass_rand = 0
#For rand column
print("=========================\nRand\n=========================")
for i in range(100):
    EVALS = 0
    print("iter", i)
    test = min_conflict_rand(initial(), 1000)
    if test == "passed":
      num_pass_rand+=1
      average_rand += EVALS



#For cyclic column
print("=========================\nCycle\n=========================")
average_cycle = 0
num_pass_cycle = 0
for i in range(100):
    EVALS = 0
    print("iter", i)
    test = min_conflict(initial(), 1000)
    if test == "passed":
      num_pass_cycle+=1
      average_cycle += EVALS

print("RANDOM:")
print("The amount passed out of 100:" , num_pass_rand)
print("The average of Evals for found Solutions: ", average_rand/num_pass_rand)

print("CYCLE:")
print("The amount passed out of 100:" , num_pass_cycle)
print("The average of Evals for found Solutions: ", average_cycle/num_pass_cycle)