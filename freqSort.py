def frequencySort(s):
    d = {}
    rs = ""
    for e in s:
        if e in d:
            d[e] = d[e] + 1
        else:
            d[e] = 1
    for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
       for i in range(0,v):
           rs = rs + k
    return rs

print(frequencySort("aacccb"))