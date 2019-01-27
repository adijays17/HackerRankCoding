def digLen(arr):
    d1=0
    d2=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                d1 = d1+arr[i][j]
            if i+j==len(arr)-1:
                d2 = d2+arr[i][j]
    dif=d1-d2
    if dif<0:
        dif = dif*-1
    return dif


print(digLen([[-1,1, -7, -8],[-10, -8, -5, -2],[0, 9, 7, -1],[4,4, -2, 1]]))