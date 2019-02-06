import math
import os
def count_rocks(ribbon_length, rocks):
    if len(rocks)==0 or ribbon_length == 0:
        return 0
    s = 0
    count = 0
    for each in rocks:
        if count == len(rocks)-1:
            s = s + math.sqrt((rocks[count][0]-rocks[count+1][0])**2 + (rocks[count][1]-rocks[count+1][1])**2)
        else:
            s = s + math.sqrt((rocks[count][0]-rocks[0][0])**2 + (rocks[count][1]-rocks[0][1])**2)
    print(s)
    return int(s/ribbon_length) +1

print(count_rocks(10.0, [[0,0],[0,3],[3,3]]))