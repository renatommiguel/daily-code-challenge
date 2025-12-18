"""Checkerboard

Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

    The characters should alternate like a checkerboard.
    The top-left cell must always be "X".

For example, given [3, 3], return:

[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]

Tests

Failed: 1. create_board([3, 3]) should return [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]].
Failed: 2. create_board([6, 1]) should return [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]].
Passed: 3. create_board([2, 10]) should return [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]].
Passed: 4. create_board([5, 4]) should return [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]].
"""


if __name__ =="__main__":
    def create_board(d:list)->list:
    #r,c
        row,col = d[0],d[1]
        mat = []
        # making first row
        xo = col * ["X"]
        for ind,_ in enumerate(xo):
            if not (ind%2==0):
                xo[ind]="O"
        ox = list(xo)
        ox.insert(0,"O")
        ox.pop(-1)
        for r in range(row):
            if r%2 == 0:
                mat.append(xo)
            else:
                mat.append(ox)
        # print(mat)
        return mat
    print(create_board([3, 3]) == [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]])
    print(create_board([6, 1]) == [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]])
    print(create_board([2, 10]) == [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]])
    print(create_board([5, 4]) == [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]])