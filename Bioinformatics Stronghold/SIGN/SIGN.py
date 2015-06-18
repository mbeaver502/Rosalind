#-------------------------------------------#
# J. Michael Beaver                         #
# 18 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/sign/       #
#-------------------------------------------#

from math import factorial
from itertools import permutations
from itertools import product

#    Author: ninjagecko
# Reference: http://stackoverflow.com/a/10803731
def plusAndMinusPermutations(items):
    for p in permutations(items):
        for signs in product([-1,1], repeat=len(items)):
            yield [a*sign for a,sign in zip(p,signs)]

f = open("rosalind_sign.txt")
n = int(f.read())
f.close()

lst = []
for i in range(1, n + 1):
    lst.append(i)

lst = list(plusAndMinusPermutations(lst))

print(len(lst))
for item in lst:
    for x in item:
        print(x, end = ' ')
    print()
