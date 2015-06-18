#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/ini4/       #
#-------------------------------------------#

a = 4060
b = 8206
nSum = 0

while (a <= b):
    if (a % 2 == 1):
        nSum += a
        a += 2
    else:
        a += 1

print(nSum)
