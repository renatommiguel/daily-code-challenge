l:list = list(range(0,100))
values = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]

with open("aoc2025/aoc1/aoc1-puzzle-input.txt", 'r') as file:
            # Read all lines from the file into a list of strings
            lines_list = file.readlines()
values = lines_list
ind:int = 50
counter:int = 0 
for v in values:
    if v.startswith("L"):
        n = int(v[1:])
        # subtract from the index
        n = int(v[1:])
        ind-=n
    else:
        # add to the index
        n = int(v[1:])
        ind+=n
    if ind > 99:# or ind <-100:
        ind = ind%100
    elif  ind <-100:
        ind = -(abs(ind)%100)
    ind = l[ind]
    if ind == 0:
        counter+=1
print(counter)    
#pass 1191
              