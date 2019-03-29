s = "ababacb"
k = 3
d = {}
max_count = 0
for e in range(0,len(s)):
    for p in range (e, len(s)):
        if s[p] in d:
            d[s[p]] = d[s[p]] + 1
        else:
            d[s[p]] = 1
        prev_count = max_count
        #check
        curr_count = 0
        for each in d:
            if d[each] >= k:
                curr_count = curr_count + d[each]
            else:
                max_count = prev_count
                curr_count = prev_count
                break
        if curr_count > max_count:
            max_count = curr_count
    d = {}

print(max_count)

