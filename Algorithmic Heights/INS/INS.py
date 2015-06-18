#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/ins/        #
#-------------------------------------------#

def sort(arr):
    count = 0
    for i in range(1, len(arr)):
        k = i
        while (k > 0 and int(arr[k]) < int(arr[k - 1])):
            temp = arr[k - 1]
            arr[k - 1] = arr[k]
            arr[k] = temp
            k -= 1
            count += 1
    return count

f = open("rosalind_ins.txt")
i = 0
for line in f:
    if (i == 1):
        lst = line.split(' ')
    i += 1
f.close()

print(sort(lst))

