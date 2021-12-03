import itertools
import math
import sys
import re

num = int(sys.argv[1])

seq = list(range(1, num + 1))
perm = itertools.permutations(seq)

print(math.factorial(num))
for i in list(perm):
    print(i)
