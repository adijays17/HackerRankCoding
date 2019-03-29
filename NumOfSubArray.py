def subarraySum(nums, k):
    count = 0
    for i in range(0, len(nums)):
        sum = nums[i]
        if sum == k:
            count += 1
        for j in range(i+1, len(nums)):
            sum += nums[j]
            if sum == k:
                count += 1
    return count

print(subarraySum([0,0,0,0,0,0,0,0,0,0] ,0))
