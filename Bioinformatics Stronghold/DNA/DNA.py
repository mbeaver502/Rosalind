#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/dna/        #
#-------------------------------------------#

s = "TTCCTCAAGCTGGAGGTCAATAAATTTCGTAGACGCGAACTAATCACTTCGTGACATGGAGTTGCTTTCCGAATCGGCGTACGTCGGGCACATGGGCAGGAGGCGGCCCAGCATTTTGCATTTGTGTTGCTCCCGAAAGTCATCCCCATGACTTGAAGGTTCCCTTTTGAGTTTTCCCATGGACATGCACCTGGGCCATCGGGTTTATCGTGTGTTTTCTTGATGGGCGGGTCCCGTAGGCCCCTAGTAGAAAGATTCGACATGCCAATTGAGGTTGAAACCCTAGATTCGATTGCCCATTACTTTTCTCCGTACTAGTGCGAATCTAGTACAGCCCGTGCTCTCTCTACACTTAGGCCGATGCCGCGGCCAGTTGATATTACTTCCTTGTCGTCACGGTAGCACTGCCGTACGCGGGATGGGCGGACGATGATGTCGCTCCAATTCTCGACAGCGTTGCGTCCTAGAGATCCGTGTGACGCACCTCATGGATACCCTAATACACCGCTAGTGCATGTGGTCCAGTTTGAGGGACATTCAGTTGAGAGGACTCTCCTTCGCGGACCCTTGCGTGACGATTTTTTGTGGGAGCTGATGGTGCATGACACCATGCACGCAAAGGCGGCTTCATGCGAGTCCTCCCACCCGACAATCAATACCGCCTGCATAAGAAGAATCGTAACCCCCTTCTCAGGCAACTGGACACGGAGTTACAGAAATGATCCGCCTACGTGTGAGCGCCGACCTTTTACCAGTGCCTAGAAGCCAGCGAAGTGATAATTACGAATATACTGAGGAATCGTGACTTATAAGATCTAATGCGAATTGTTGGGCGAGTGCAGAGGTAGATTTGGTTACGACTGTAGCTCTCAGCGTTGTCGGTACGCAAATCAGTCAAGCCTGCGCTAGGGACAGTGGAGCCGCCATGATGATTCGCCGTCAATCTGTCGGGCGATCGCTTCTCCCAGCACGCAGGCCTAGCTTTTTGGG"
idx = 0
size = len(s)
d = dict()

while (idx < size):
    nt = s[idx]
    if (nt in d):
        d[nt] = d.get(nt) + 1
    else:
        d[nt] = 1
    idx += 1

for key, value in d.items():
    print(key, value)
