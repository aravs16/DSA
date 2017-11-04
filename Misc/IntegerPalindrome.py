import math
def is_integer_pal(n):

    d = int(math.log(n,10))+1
    m = d//2
    sum = 0

    for i in range(0,m):
        sum = sum+(n%10)
        n = n//10

    if(d%2 != 0):
        n = n//10

    for i in range(m,d):
        sum = sum-(n%10)
        n = n//10

    return sum

i = int(input())
print('Palindrome' if is_integer_pal(i) == 0 else 'Not Palindrome')
