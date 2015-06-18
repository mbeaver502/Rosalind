#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/ini5/       #
#-------------------------------------------#

f = open("rosalind_ini5.txt")
idx = 1
lines = []

for line in f:
    if (idx % 2 == 0):
        lines.append(line)
    idx += 1
f.close()

f = open("data.txt", "w")
for item in lines:
    f.write(item)
f.close()
