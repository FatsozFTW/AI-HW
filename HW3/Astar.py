m_row = 100 # 0-3
m_col = 100 # 0-7

fringe_c = 0
closed_c = 0
#row = int(input("size of row: "))
#col = int(input("size of col: "))
v = [[0 for x in range(m_col)] for y in range(m_row)]

#obstacle

init = 75
jinit = 70
igoal = 50
jgoal = 55

start = (0, init, jinit)
end = (0, igoal, jgoal)

grid = [[0 for x in range(m_col)] for y in range(m_row)] # initialize to "no obstacles"

for i in range(100):
    for j in range(100):
        if i < 50:    # rear of bugtrap
            d = abs(i-51) + abs(j-50)
            if d == 50:
                grid[i][j] = 1
        else:        # front of bugtrap
            if j > 50:  # upper lobe
                d = abs(i-50) + abs(j-75)
                if d==24:
                    grid[i][j]=1
            elif j < 50:  # lower lobe
                d = abs(i-50) + abs(j-25)
                if d == 24:
                    grid[i][j] = 1
grid[igoal][jgoal] = 'E'

def mark_visited(node, v):
    v[node[1]][node[2]] = 1

def get_neighbors(node, grid):
    global fringe_c
    temp = []
    temp2 = []
    row = node[1]
    col = node[2]
    #h = []
    choice = 0
    #up
    if(row-1 >= 0 ):
        if(grid[row-1][col] != 1):
            if is_visited((0, row-1, col), v) is False:
                h_cost = abs(row-1-start[1]) + abs(col-start[2])+abs(row-1-end[1]) + abs(col - end[2])
                #h.append(h_cost)
                temp.append((h_cost, row-1, col))
                fringe_c= fringe_c+ 1


    #down
    if(row+1 <= m_row-1 ):
        if(grid[row+1][col] != 1):
            if is_visited((0, row+1, col), v) is False:
                h_cost = abs(row+1-start[1]) + abs(col-start[2])+abs(row+1-end[1]) + abs(col - end[2])
                #h.append(h_cost)
                temp.append((h_cost, row+1, col))
                fringe_c=fringe_c+1


    #left
    if(col-1 >= 0 ):
        if(grid[row][col-1] != 1):
            if is_visited((0, row, col-1), v) is False:

                h_cost = abs(row-start[1]) + abs(col -1-start[2])+abs(row-end[1]) + abs(col -1 - end[2])
                #h.append(h_cost)
                temp.append((h_cost, row, col-1))
                fringe_c=fringe_c+1


    #right
    if(col+1 <= m_col-1 ):
        if(grid[row][col+1] != 1):

            if is_visited((0, row, col+1), v) is False:
                h_cost = abs(row-start[1]) + abs(col +1-start[2])+abs(row-end[1]) + abs(col +1 - end[2])
                #h.append(h_cost)
                temp.append((h_cost, row, col+1))
                fringe_c=fringe_c+1


    temp.sort(reverse=False)
    #(x,y)
    return(temp)

def is_visited(node, v):
    #print("in is visited: ", node)
    row = node[1]
    col = node[2]
    if(v[row][col] == 1):
        return(True)
    else:
        return(False)

def astar(start, grid):
    global closed_c
    global fringe_c
    queue = list()
    path = list()
    queue.append(start)
    closed_c=closed_c +1
    fringe_c-=1
    while len(queue) > 0:
        node = queue.pop(0)
        path.append(node)
        mark_visited(node, v)

        if grid[node[1]][node[2]] == 'E':
            fringe_c-=1
            closed_c-=1
            break
        adj_nodes = get_neighbors(node, grid)
        closed_c=closed_c +1
        fringe_c-=1
        for item in adj_nodes:
            if is_visited(item, v) is False and item not in queue:
                queue.append(item)
                queue.sort(reverse=False)
    return path           

paths = astar(start, grid)
print("printing path: ")
print(paths)
print("length of path: ")
print(len(paths))
print("closed :", closed_c)
print("fringe: ", fringe_c)