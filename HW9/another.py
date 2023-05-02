from mdp_temp import mdpFunc,T
class temporary:
    def __init__(self, R, T, G, actions, TDict) -> None:
        self.gamma = G
        self.R = R
        self.T = T
        self.states = [1,2,3,4,5,6,7,8,9]
        self.TDict = TDict
        self.actions = actions
        
def tryme(state):
    arr = set()
    for a in [1,2,3,4]:
       # print("cosmic divide-------")
        for snext in [1,2,3,4,5,6,7,8,9,10,11]:
            s1, p = T(state, a, snext, mdpFunc())
            if(s1 != 0):
                arr.add(snext)
                #print("this is snext:", snext)
    return arr  
def R():
    return -1
        
def value_iteration(mdp, epsilon=0.001):
    "Solving an MDP by value iteration. [Fig. 17.4]"
    U1 = dict([(s, 0) for s in mdp.states])
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    iter = 0
    for x in range(500):
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            temp = 0
            maxarr = []
            for a in mdp.actions:
                for snext in tryme(s):
                        s1, p = T(s, a, snext, mdpFunc())
                        if s1 != 0:
                            if s1 == 10:
                                temp += p * -1
                            elif s1 == 11:
                                temp += p * 1
                            else:
                                temp += p * U[s1]
                maxarr.append(temp)           
           
            U1[s] = R() + gamma * max(maxarr)
                                        
            delta = max(delta, abs(U1[s] - U[s]))
        iter +=1
        print("iter:", iter)

    return U

def expected_utility(a, s, U, mdp):
    temp= 0
    for snext in tryme(s):
        s1, p = T(s, a, snext, mdpFunc())
        if s1 != 0:
            if s1 == 10:
                temp += p * -1
            elif s1 == 11:
                temp += p * 1
            else:
                temp += p * U[s1]
    return temp

def best_policy(mdp, U):
    """Given an MDP and a utility function U, determine the best policy,
    as a mapping from state to action. (Equation 17.4)"""
    pi = {}
    temparr = []
    for s in mdp.states:
        for a in mdp.actions:
            temparr.append(expected_utility(a, s, U, mdp))
        pi[s] = max(temparr)
    return pi

actions = [1,2,3,4]
temp = temporary(R, T, 1, actions, mdpFunc())

hi = value_iteration(temp)
bye = best_policy(temp, hi)
print(hi)
print("-----------------------------------")
print(bye)





def test(state):
    arr = set()
    for a in [1,2,3,4]:
        print("cosmic divide-------")
        for snext in tryme(state):
            s1, p = T(state, a, snext, mdpFunc())
                
            print(s1, p)
    return arr  
#test(1)
#tryme(1)

"""
U1[s] = R() + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a, snext, mdpFunc())])
                            for a in mdp.actions for snext in [1,2,3,4,6,7,8,9,10,11]] )
"""