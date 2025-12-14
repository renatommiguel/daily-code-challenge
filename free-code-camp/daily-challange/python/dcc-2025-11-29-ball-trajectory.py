"""
Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the ball hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.

get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) # should return [2, 3].
get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) # should return [3, 0].
get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) # should return [1, 2].
get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) # should return [1, 1].
get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) # should return [2, 2].

"""

def printm(m):
    print(f"rc 0  1  2  3 ")
    for r, row in enumerate(m):
        print(r, row)
def get_direction(dold,dcur):
    # present - past
    # if positive going from left to right
    # top to bottom
    # if negative, reversed movement
    # if 0, no change in the 0 direction
    ddir = {}
    ddir['row'] = dcur['row'] - dold['row']
    ddir['col'] = dcur['col'] - dold['col']
    return ddir

def calc_fut(dcur,ddir,lenmat,dfut):
    if dcur['row']>=(lenmat-1) or dcur['row']<=0 :
        ddir['row'] = ddir['row'] * (-1)
    if dcur['col']>=(lenmat-1) or dcur['col']<=0 :
        ddir['col'] = ddir['col'] * (-1)
    dfut['col'] = dcur['col'] + ddir['col'] 
    dfut['row'] = dcur['row'] + ddir['row'] 
    return dfut
    
def get_next_location(matrix):
    lenmat=len(matrix)
    ddir={"row":None,"col":None}
    dfut={"row":None,"col":None}
    dcur={"row":None,"col":None}
    dold={"row":None,"col":None}
    for r, row in enumerate(matrix):
        if 1 in row:
            dold['row'] = r
            dold['col'] = row.index(1)
        if 2 in row:
            dcur['row'] = r
            dcur['col'] = row.index(2)
    ddir = get_direction(dold,dcur)
    dfut = calc_fut(dcur,ddir,lenmat,dfut)
    printm(matrix)
    return list(dfut.values())



if __name__=="__main__":
    get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) # should return [2, 3].
    # get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) # should return [3, 0].
    # get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) # should return [1, 2].
    # get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) # should return [1, 1].
    # get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) # should return [2, 2].
