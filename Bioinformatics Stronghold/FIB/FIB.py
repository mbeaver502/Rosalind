#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/fib/        #
#-------------------------------------------#

fibs = [1, 1]

def fib(n, k):
    if (n > len(fibs) + 1):
        fib(n - 1, k)
    x = fibs[n-2] + (k * fibs[n - 3])
    fibs.insert(n - 1, x)
    return x


n = 28
k = 2

print(fib(n, k))
