envChoice = ["Dirty", "Clean"]
pos = ["A","B"]
env = []
test = []
TestCounter = 0
performanceCounter = 0
#initial environments
for i in pos:
    for x in range(2):
        for y in range(2):
            env.append([i, envChoice[x],envChoice[y]])
print(env)
print(env[1][2])

#The look up table
def lookup(env2):

    if env2[0] == "A" and env2[1] == "Clean":    #A, Clean
        env2[0] = "B"
        return(["Right", env2])
    elif env2[0] == "A" and env2[1] == "Dirty":  #A, Dirty
        env2[1] = "Clean"
        return(["Suck", env2])
    elif env2[0] == "B" and env2[2] == "Clean":  #B, Clean
        env2[0] = "A"
        return(["Left", env2])
    elif env2[0] == "B" and env2[2] == "Dirty":  #B, Dirty
        env2[2] = "Clean"
        return(["Suck", env2])

def checkClean(given, counter):
    if given[1] == "Dirty":
        counter+=1
    if given[2] == "Dirty":
        counter+=1
    return(counter)

#Testing all 8
for y in env:
    #Test of 1-8
    TestCounter+=1
    performanceCounter = 0
    print("Doing test: ", TestCounter)
    currentPos = y[0]
    print("Current state: ", y)
    #Run for a number of steps: 10
    for z in range(10):
        #run lookup
        action = lookup(y)
        #y = action[1]
        print("Action taken: ", action[0], y)
        performanceCounter = checkClean(y, performanceCounter)
    test.append(performanceCounter)

print(test)
        