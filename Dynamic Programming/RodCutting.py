# Non Efficient Algorithm

def cut_rod(p, n):
    if n == 0:
        return 0
    q = -9999999

    for i in range(1,n+1):
        q = max(q,p[i-1]+cut_rod(p,n-i))

    return q


p = [1,12,3,4]
n = 4

print(cut_rod(p,n))
