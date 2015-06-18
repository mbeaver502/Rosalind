#-------------------------------------------#
# J. Michael Beaver                         #
# 17 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/iprb/       #
#-------------------------------------------#

from math import factorial
from itertools import combinations

hod = 'AA'
hed = 'Aa'
hor = 'aa'

k = 23
m = 22
n = 18
pop = k + m + n

lst = []
for i in range(0, k):
    lst.append(hod)
for i in range(0, m):
    lst.append(hed)
for i in range(0, n):
    lst.append(hor)
c = list(combinations(lst, 2))

# The expected value is nCr * 4, where n = total population and r = 2.
# We multiply by 4 because Punnett Squares have 4 cells.
exp = (factorial(pop) / (factorial(pop - 2) * factorial(2))) * 4
obs = 0

for item in c:
    if ((item[0] == hod and item[1] == hod) or
        (item[0] == hod and item[1] == hed) or
        (item[0] == hed and item[1] == hod) or
        (item[0] == hod and item[1] == hor) or
        (item[0] == hor and item[1] == hod)):
        obs += 4
    elif (item[0] == hed and item[1] == hed):
        obs += 3
    elif ((item[0] == hed and item[1] == hor) or
          (item[0] == hor and item[1] == hed)):
        obs += 2

print(obs/exp)
