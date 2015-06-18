#-------------------------------------------#
# J. Michael Beaver                         #
# 17 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/grph/       #
#-------------------------------------------#

f = open("rosalind_grph.txt")
lst = f.read()
f.close()

lst = lst.replace('\n', '')
lst = lst.split('>')
dna = []
graph = []

for item in lst:
    if (len(item) < 1):
        continue
    k = item[0:13]
    v = item[13::]
    dna.append((k, v))

for i in range(0, len(dna)):
    suffix = dna[i][1][-3::]
    for j in range(0, len(dna)):
        if (i != j):
            prefix = dna[j][1][0:3]
            if (suffix == prefix):
                graph.append((dna[i][0], dna[j][0]))

for item in graph:
    print(item[0], item[1])
        


