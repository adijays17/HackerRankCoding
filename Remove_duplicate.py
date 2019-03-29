def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    count = 0
    for i in range(1, len(nums)):
        if nums[count] == nums[i]:
            count += 1
            nums[count] = nums[i]
    return count, nums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))