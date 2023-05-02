import math
import random
#Initial Variables
n=10
first_gen = []
new_gen = []
#The function we want to maximize
def fitness(x):
    return 4+2*x +2*math.sin(20*x) - 4*x*x

#Initialize generation
for i in range(n):
    #K random 0-100
    k = random.randrange(0,100)
    #random selection of individuals
    r = k*0.01
    first_gen.append(r)
#The amount of generations wanted
gen = 50


def parent_select():
    TF = 0
    for i in range(len(first_gen)):
        TF += fitness(first_gen[i])
    pick = random.uniform(0,TF)
    current = 0
    for x in first_gen:
        current += fitness(x)
        if current > pick:
            return x

def mutation():
    a = random.random()
    p1 = parent_select()
    p2 = parent_select()
    while(p1 != p2):
        p2 = parent_select()
    return a*p1 + (1-a)*p2


def run():
    #Runs each generation
    for generation in range(gen-1):
        #Runs for each individual
        new_gen = []
        for x in first_gen:
            new_gen.append(mutation())

        #Replace old with new
        for i in range(n):
            if new_gen[i] < 0:
                #removing negatives
                first_gen[i] = random.random()
            else:
                #else replace old gen with new gen
                first_gen[i] = new_gen[i]
        

print(first_gen)

run()
print(first_gen)