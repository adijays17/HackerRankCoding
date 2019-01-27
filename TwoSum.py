def twoSum(nums, target):
    for i in range(0, len(nums)):
        if target-nums[i] in nums and i != nums.index(target-nums[i]):
            return [i, nums.index(target-nums[i])]

print(twoSum([3,2,4], 6))