#-------------------------------------------#
# J. Michael Beaver                         #
# 16 June 2015                              #
#-------------------------------------------#
# No attempt has been made to optimize this #
# code. There may be no error-checking.     #
#-------------------------------------------#
# http://rosalind.info/problems/fibo/       #
#-------------------------------------------#

fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n < len(fibs)):
        return fibs[n]
    else:
        if (n > len(fibs)):
            fib(n - 1)
        x = fibs[n - 1] + fibs[n - 2]
        fibs.insert(n, x)
        return x


n = 25

print(fib(n))
print(fibs)
