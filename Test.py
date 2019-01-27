def checkPossibility(nums):
    count = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[i]>nums[j]:
                count += 1
                print(nums[i])
                break
        if count>=2:
            return False
    return True

print(checkPossibility([2,3, 3, 2, 4]))