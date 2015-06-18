#-------------------------------------------#
# J. Michael Beaver                         #
# 17 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/perm/       #
#-------------------------------------------#

from math import factorial
from itertools import permutations

n = 6
nf = factorial(n)

lst = []
for x in range(1, n + 1):
    lst.append(x)
t = set(permutations(lst))

print(nf)
for item in t:
    print(item)
