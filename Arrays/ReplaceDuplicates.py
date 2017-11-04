def removeDups(ar):
    l = len(ar)
    i = 0
    j = 1

    while j < l:
        if ar[j] != ar[i]:
            for k in range(i+1,j):
                ar[k] = ar[j]
            i = i + 1
        else:
            j = j + 1
    return ar


ar = [1,2,2,3,4,5,5,5,6]
ar = removeDups(ar)
print(ar)
