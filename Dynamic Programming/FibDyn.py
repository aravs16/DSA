def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

# 0 1 1 2 3 5 8 13
print(fib(6))


def fibdyn(n,mem):
    if n <= 1:
        return n
    elif n in mem:
        return mem[n]
    else:
        k = fibdyn(n-1,mem)+fibdyn(n-2,mem)
        mem[n]=k
        return k
mem={}
print(fibdyn(6,mem))


def fibdyn_tab(n):
     tab = {}
     tab[0] = 0
     tab[1] = 1
     i = 2
     while i <= n:
         tab[i] = tab[i-1]+tab[i-2]
         i = i+1

     return tab[n]

print(fibdyn_tab(6))
