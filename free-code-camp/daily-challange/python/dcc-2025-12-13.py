"""
Game of Life
Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

Each cell is either 1 (alive) or 0 (dead).
A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
Cells on the edges have fewer than eight neighbors.
Rules for updating each cell:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors lives on.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes alive (reproduction).
For example, given:

[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]
return:

[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]
Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.


game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]) # should return [[0, 1, 1], [0, 0, 1], [1, 1, 1]].
game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]) # should return [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]].
game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) # should return [[0, 0, 0], [0, 1, 0], [0, 0, 0]].
game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]) # should return [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]].

"""
def count_neigh(row,col,grid):
    neigh = []
    r = []
    c = []
    # find R
    if row==0:
        r = [row, row+1]
    elif row == len(grid)-1:
        r = [row-1, row]
    else:
        r = [row-1, row, row+1]
    # fiend C
    if col==0:
        c = [col, col+1]
    elif col == len(grid)-1:
        c = [col-1, col]
    else:
        c = [col-1, col, col+1]
    for rr in r:
        for cc in c:
            if not (cc==col and row==rr):
                neigh.append(grid[rr][cc])
    return neigh
def live(sn):
    if sn < 2:
        # print("underpop")
        return 0
    elif 2<=sn<=3:
        # print('liveon')
        return 1
    else:
        # print("op")
        return 0

def dead(sn):
    if sn==3:
        # print('reproduce')
        return 1
    else:
        # print('stay dead')
        return 0

def update_status(ele, sum_neigh):
    # print('update')
    if ele:
        res = live(sum_neigh)
    else:
        res = dead(sum_neigh)
    return res

def game_of_life(grid):
    newgrid = []
    for row, arr in enumerate(grid):
        newcol=[]
        for col, ele in enumerate(arr):
            neigh = count_neigh(row,col,grid)
            sum_neigh = sum(neigh)
            res = update_status(ele, sum_neigh)
            newcol.append(res)
        newgrid.append(newcol)
        print(newcol)
    print(newgrid)
    return newgrid

if __name__=="__main__":
    game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]])
