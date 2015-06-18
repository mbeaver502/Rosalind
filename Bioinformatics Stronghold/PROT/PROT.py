#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/prot/       #
#-------------------------------------------#

def to_protein(s):
    p = str()
    i = 0
    
    while (i < len(s)):
        t = s[i:i+3]
        if (t == "UUU" or t == "UUC"):
            p += "F"
        elif (t == "UUA" or t == "UUG" or
              t == "CUU" or t == "CUC" or
              t == "CUA" or t == "CUG"):
            p += "L"
        elif (t == "UCU" or t == "UCC" or
              t == "UCA" or t == "UCG" or
              t == "AGU" or t == "AGC"):
            p += "S"
        elif (t == "UAU" or t == "UAC"):
            p += "Y"
        elif (t == "UGU" or t == "UGC"):
            p += "C"
        elif (t == "UGG"):
            p += "W"
        elif (t == "CCU" or t == "CCC" or
              t == "CCA" or t == "CCG"):
            p += "P"
        elif (t == "CAU" or t == "CAC"):
            p += "H"
        elif (t == "CAA" or t == "CAG"):
            p += "Q"
        elif (t == "CGU" or t == "CGC" or
              t == "CGA" or t == "CGG" or
              t == "AGA" or t == "AGG"):
            p += "R"
        elif (t == "AUU" or t == "AUC" or
              t == "AUA"):
            p += "I"
        elif (t == "AUG"):
            p += "M"
        elif (t == "ACU" or t == "ACC" or
              t == "ACA" or t == "ACG"):
            p += "T"
        elif (t == "AAU" or t == "AAC"):
            p += "N"
        elif (t == "AAA" or t == "AAG"):
            p += "K"
        elif (t == "GUU" or t == "GUC" or
              t == "GUA" or t == "GUG"):
            p += "V"
        elif (t == "GCU" or t == "GCC" or
              t == "GCA" or t == "GCG"):
            p += "A"
        elif (t == "GAU" or t == "GAC"):
            p += "D"
        elif (t == "GAA" or t == "GAG"):
            p += "E"
        elif (t == "GGU" or t == "GGC" or
              t == "GGA" or t == "GGG"):
            p += "G"
        elif (t == "UAA" or t == "UAG" or
              t == "UGA"):
            return p
        i += 3

    return p

f = open("rosalind_prot.txt")
s = f.read()
f.close()
print(to_protein(s))
