#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/prtm/       #
#-------------------------------------------#

def mim_weight(s):
    w = 0
    for a in s:
        if (a == 'A'):
            w += 71.03711
        elif (a == 'C'):
            w += 103.00919
        elif (a == 'D'):
            w += 115.02694
        elif (a == 'E'):
            w += 129.04259
        elif (a == 'F'):
            w += 147.06841
        elif (a == 'G'):
            w += 57.02146
        elif (a == 'H'):
            w += 137.05891
        elif (a == 'I'):
            w += 113.08406
        elif (a == 'K'):
            w += 128.09496
        elif (a == 'L'):
            w += 113.08406
        elif (a == 'M'):
            w += 131.04049
        elif (a == 'N'):
            w += 114.04293
        elif (a == 'P'):
            w += 97.05276
        elif (a == 'Q'):
            w += 128.05858
        elif (a == 'R'):
            w += 156.10111
        elif (a == 'S'):
            w += 87.03203
        elif (a == 'T'):
            w += 101.04768
        elif (a == 'V'):
            w += 99.06841
        elif (a == 'W'):
            w += 186.07931
        elif (a == 'Y'):
            w += 163.06333

    return w
            
f = open("rosalind_prtm.txt")
s = f.read()
f.close()
print(mim_weight(s))
