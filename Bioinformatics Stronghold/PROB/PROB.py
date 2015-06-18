#-------------------------------------------#
# J. Michael Beaver                         #
# 18 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/prob/       #
#-------------------------------------------#

from math import log

def count_nt(dna):
    count_at = 0
    count_gc = 0
    for i in range(0, len(dna)):
        if (dna[i] == 'A' or dna[i] == 'T'):
            count_at += 1
        elif (dna[i] == 'G' or dna[i] == 'C'):
            count_gc += 1
    return (count_at, count_gc)

f = open("rosalind_prob.txt")
lst = f.read()
f.close()

lst = lst.split('\n')
dna = lst[0]
lst = lst[1].split(' ')
probs = []
counts = count_nt(dna)

for prob in lst:
    pGC = float(prob) / 2
    pAT = (1 - float(prob)) / 2
    p = (pAT**counts[0]) * (pGC**counts[1])
    probs.append(log(p, 10))

for p in probs:
    print(p, end = ' ')
