# Non Efficient Algorithm

def cut_rod(p, n):
    if n == 0:
        return 0
    q = -9999999

    for i in range(1,n+1):
        q = max(q,p[i-1]+cut_rod(p,n-i))

    return q

def cut_rod_mem_1(p,n,r):

    if n == 0:
        return 0
    if r[n] >= 0:
        return r[n]
    else:
        q = -99999999
        for i in range(0,n):
            q = max(q, p[i]+cut_rod_mem_1(p,n-i-1,r))
        r[n] = q

    return r[n]

def cut_rod_mem_2(p,n,r):

    r[0] = 0
    for i in range(0,n):
        q = -9999999

        for j in range(0,i):
            q = max(q,p[i-j]+r[j])

        r[i+1] = q

    return r[n]

p = [1,12,3,4]
n = 4

# print(cut_rod(p,n))

r = {}
for i in range(1,n+1):
    r[i] = -1
print(cut_rod_mem_2(p,n,r))
