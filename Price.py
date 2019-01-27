#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculateAmount' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def calculateAmount(prices):
    total = 0
    minimum = 0
    for i in range(0, len(prices)):
        if i == 0:
            total += prices[i]
            minimum = prices[i]
        else:
            total +=  max(prices[i]-minimum, 0)
            if prices[i] < minimum:
                minimum = prices[i]
    return total

print(calculateAmount([4,9,2,3]))
