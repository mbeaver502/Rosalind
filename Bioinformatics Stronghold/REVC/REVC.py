#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/revc/       #
#-------------------------------------------#

s = "CCTAGTACGGCAGTAGCCGTTTGTCATAACTTTCGATGTAATTCGTGAATAAAGCATCCAAGTATTCATACCGATTAAATTACGGTCGAGCTGCTCCCGGCCCCCAGATGTGACTCGTATACCTGGATTAGACAGGCGTAACTAGGTTCAGGTCGATCTGAGCGTGTCTTAAGTTGGGTAGGGCTCGTAATATAACTGGCCGGGCGCGGAAAGTATCCGCAGGTTTCTAATTTCGGCGGATGAGCATAATTTCTGATGCAACTACTGAACGTGAGGGTTGGTTGAAATTGTAGGTGAGGACTTTTTTTTGGAGCACTTGGCCACCAATATCGCCGTACATTAAGTATCGCCCCAGGTTATTCGTCGTTCTGTGTACGTGAACTTGGCACTACGGTGCAAATTCACAATTTTCTCTGGCGGGAGATTAAACGCGCTCCTTCTGTGGGATAGGATAGTCTAGGGCAATGGTCGCGGCAAAACCTATGCAAACTAGTGTCGTCGTCCCAAACGCAAACTTGGATCACAACCCGTCCTTTCGTTAATATAAACGCTCGGCTCCGTCGAGGAAAATAGAATATGCTTTGCGTTTAGTGCGCTTGGGGCATTCGATAGAAAAGCAGCACAGTCGGTTATCCTACTTAACTATCGAGCATTACCCTTCGTGGACGCCTCCACAAAAATTCACCCCCACAGGTTGAAGCTCCGCATTTGCCAATTGTGAATAGTTCCCGTTGGTCGCAAAGTCCAATATTAGATTGATGGTCGCAATAGTACAGGCTGGAAAACGGGTAGAGCTCTAGATAAAAATATGCGCCTGACTTTCCTTGAATGGGGACGAGCGCGGGCTACGCGCTCCAGCCAATGCTCCTGGGTCCCCCTCG"
s = s[::-1]
sc = str()

for b in s:
    if (b == 'A'):
        sc += 'T'
    elif (b == 'T'):
        sc += 'A'
    elif (b == 'G'):
        sc += 'C'
    elif (b == 'C'):
        sc += 'G'

print(sc)
