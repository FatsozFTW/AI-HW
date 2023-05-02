"""
inputs x1 x2 x3    output
----------------   ------
        1  0  0      1
        0  1  1      0        
        1  1  0      1
        1  1  1      0
        0  0  1      0
        1  0  1      1                        
"""
#update this if changing width
size = 5
counter = 0
data = [
    [-1,1,0,0,1],
    [-1,0,1,1,0],
    [-1,1,1,0,1],
    [-1,1,1,1,0],
    [-1,0,0,1,0],
    [-1,1,0,1,1]
]
N = len(data)
#change depending on # of inputs
_weight = [0,0,0,0]

def netoutput(x_num):
    sum = 0
    X = data[x_num]
    for i in range(len(X)-1):
        sum += _weight[i] * X[i]
    if sum > 0:
        return 1
    else:
        return 0

def weight_calc(check, xi):
    global counter
    if check == 0:
        counter +=1
    else:
        for i in range(len(_weight)):
            _weight[i] = _weight[i] + check * xi[i]

# w <- w + (output - netoutput) * X
def weight_update():
    global counter
    while counter != N:
        counter = 0
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        for xi in range(len(data)):
            print("X%d" % (xi+1))
            Yi = data[xi][size-1]
            check = Yi-netoutput(xi)
            weight_calc(check, data[xi])
            print(_weight)
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-\n")        
    print("Final weight:", _weight)
        
        
weight_update()
#print(netoutput(0))