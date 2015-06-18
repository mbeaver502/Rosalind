#-------------------------------------------#
# J. Michael Beaver                         #
# 17 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/gc/         #
#-------------------------------------------#

f = open("rosalind_gc.txt")
lst = f.read()
f.close()

lst = lst.replace('\n', '')
lst = lst.split('>')

for item in lst:
    if (len(item) < 1):
        continue
    
    k = item[0:13]
    v = item[13::]
    
    count = 0
    for nt in v:
        if (nt == 'C' or nt == 'G'):
            count += 1
    content = (count / len(v)) * 100
    
    print(k)
    print(content)



