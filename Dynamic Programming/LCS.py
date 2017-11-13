# Recusrive approach. Exponential time!
def find_lcs(s1,s2):

    print('Computing',s1,s2)

    i1 = len(s1)
    i2 = len(s2)

    if i1 <= 0 or i2 <=0:
        return 0

    if s1[i1-1] == s2[i2-1]:
        return 1+find_lcs(s1[:i1-1],s2[:i2-1])
    else:
        return max(find_lcs(s1[:i1],s2[:i2-1]), find_lcs(s1[:i1-1],s2[:i2]))


s1 = 'ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'
s2 = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'
# print(find_lcs(s1,s2)) 


# Dynamic Programming. Tabulation bottom up.
def find_seq(di,s1,s2):
    i = len(s1)
    j = len(s2)
    s = ""

    while i > 0:
        if i == 0 or j == 0:
            return s
        while j > 0:
            if i == 0 or j == 0:
                return s
            if di[i][j] == 'D':
                s = s1[i-1]+s
                i = i-1
                j = j-1
            elif di[i][j] == '|':
                i = i-1
            elif di[i][j] == '-':
                j = j-1
            else:
                print(di[i][j])

    return s



def lcs_dyn_tab(s1, s2):

    i1 = len(s1)+1
    i2 = len(s2)+1

    tab = []
    di = []

    for k in range(0,i1):
        cols = []
        for l in range(0,i2):
            cols.append(0)
        tab.append(cols)

    for k in range(0,i1):
        cols = []
        for l in range(0,i2):
            cols.append('*')
        di.append(cols)

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                tab[i][j] = tab[i-1][j-1]+1
                di[i][j] = 'D'
            elif tab[i][j-1] >= tab[i-1][j]:
                tab[i][j] = tab[i][j-1]
                di[i][j] = '-'
            else:
                tab[i][j] = tab[i-1][j]
                di[i][j] = '|'

    print(tab[i1-1][i2-1])
    k = find_seq(di, s1, s2)
    print(k)


lcs_dyn_tab("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA","GTCGTTCGGAATGCCGTTGCTCTGTAAA")
