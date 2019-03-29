def twoSum(nums, target):
    index = []
    for each in nums:
        if (target-each) in nums:
            index.append(nums.index(each))
            index.append(nums.index(target-each))
            return index

print(twoSum([2,7,11,15], 13))