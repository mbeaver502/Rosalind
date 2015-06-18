#-------------------------------------------#
# J. Michael Beaver                         #
# 17 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/lexf/       #
#-------------------------------------------#

# Incidentally, the product (Cartesian Product) function gives us the result
#  in lexographical order as it generates the product in that order (i.e.,
#  iterating over the list in order).
from itertools import product

n = 3
lst = ['T', 'B', 'R', 'N', 'W', 'U', 'A', 'K']
t = product(lst, repeat=n)

for item in t:
    print(item)
