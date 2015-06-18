#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/hamm/       #
#-------------------------------------------#

def hamming(s, t):
    count = 0
    for i in range (0, len(s)):
        if (s[i] != t[i]):
            count += 1
    return count

s = "GGCTAGCTTCCGCTCTGTAGTCGGAAGAAATCATAATTTTGGAGGTCGAACTTCATTGGTCTGACCAAGGTCACACTTCCCTGCCATTGGCTAGATAATCAGGTCCCGCAAGCACCCAGCTGTAGAATACCCGGTTTATGGATGGTGGCATGCGGTATAGCCATCTCTTTTATAGCCTTAAGTCGAGATCTGGAAAAGGGGCTCGATCTGCGCAAGCAATAGGTTTCTAGCCCCTATTTCACAAAGACGAAGCCCAGATCTTTCGCTGACCTGTGGCGGATGGGGGCTTCGCGGGGGTTCGAACTGACCAGCTTATTCTGAATGGCAGCATGTGACCCGTTGTCCCTAGTTAGCATCAAGAGAGATCACCACCGTGCCCTTGGATCTTGAGGTCATTCCGATCGGCATCATATGAGAGTTCAGCACGGCACACATGACTGTGCTCATTCAAATTGGTATCTACTCTGGTAGCGGTGACAGGAACCAGGTCATGAAAACCGGTGACCAAACTATCGCGACGGACATGTCCAAAGGCATACCAAGAATTACACTGCAACGCGTCGAACTTACTAGCGATAGTGCTCGGCGCGCTGGTGTCCTCCGGGAGATTGATTATCACGTTGACTCGATCATGTTGGAACTCCTGTCACCTATGTTTGCACCCGTTTAGCAGCAAACCGTTAGGGCAACGAACTGTTTTGAGCGTTATCGGAAGAGACAGTGGTAAAGAGCCTCCCAAACCAAAGGGTGTAGTTGGTAAATTATGCACTTTCATGACGTCTGTGGATTTGGCCATTATCATATCGCTTTAGGGGTTGCTGTTGTCCTTACCTTTGATGATCCCAGGTCCCATCGATTCCGGCGGGCCAGCGTTTCCTAACTATGTATTAACAATCGTATGAAGCCTTGACGATATGATACTACCTAGATGTCTCATAAATATTCCAGCCAGAACTTTTCAAGGTCTGCATCTTAACCACTCGTCGAGG"
t = "GGATAGCTTTGACTCGGAAACCGTAATTTCTCTTAAGCAAGAACGCCGACCCTAATGCAAGTGCGTAAGTCGCAAGGTTTCGCCGATTGTTCGGTGAAACCGGATTGCTATGCGCATAGTGGCGGGATACCCAGTTTGGCCCCGGTGAACAACTCTGTAGTCTGCGTTTTTGTAGACTTGACTTGAGCAACCAATGGCGCGATTTATCACTGGACGCGATACGTTACAACACCCTGTCCTTCCGAGATCTAGGTCCGATCTTTCTCCGCACTCAGGTAAAAGGTAAGATTTAGGGGGCTGAAGATAATCCCCCAAGTCGGACAGCCGGCGGGTGACCCGGCGAATCGGCTTCGTGACGCTACTAGCCGTACTCGAGCTACTGTACATTTTTGACTATACCATCGGGGTACTACAAGCAGTTTGCAATGCACGCCTCACTGGACAGATTCGGATACCTTGTGCCGTCAAGCGCGCTGATAAGGAACAGTTCATGGTCTACGCTCTCCAATCAAACGGTGTAAACAGGTTCATTGACTTGCCATGAATTGCACATTAACGCGCCATAATGATAGGCTAGACTTCTCTGTTCATCGGAGGCATCCGGGTACTTTCTACGCACTTTTAATTGATCATCATGGAACCACCGCTCTCTAGGTGCGCATACCTAAACTTTCGAGGCTTGTGGGCAACTAACTTGGTGTGTCGCCACCGGAAATGACGTGGCAAACAAGGGTCCGAAAGCTGAGGCCGGCTTATGTGCATTCTACGACTTCAAGAATCTAATGGATTTGGTAACTATTTGCGGGATGGCCGCGATGCATTCTACCAGTGCTACGCTGACCTGATAGCTGACGGCTTGGCTCACGTTAGCATGTAGCATCTAGGTCTTCGATAACGTACTTGGGGTTCTCTCTATGTTAATTGACACCTGTCTCATGACTCATCGAGCCACCATACACGCGGGCATGCTTTTGTACGGCTCGTACCTC"

print(hamming(s, t))