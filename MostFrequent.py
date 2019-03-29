def topKFrequent(nums, k):
    d = {}
    for e in nums:
        if e in d:
            d[e] = d[e] + 1
        else:
            d[e] = 1
    return sorted(d, key=d.get, reverse=True)[:k]

print(topKFrequent([1,1,1,2,2,2,3,3], 4))