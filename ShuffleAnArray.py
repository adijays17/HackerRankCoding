import random

class Solution:
    all_num = []
    old_num = []
    def __init__(self, nums: 'List[int]'):
        self.all_num = []
        self.old_num = []
        self.all_num = nums
        for e in nums:
            self.old_num.append(e)

    def reset(self) -> 'List[int]':
        """
        Resets the array to its original configuration and return it.
        """
        return self.old_num
        

    def shuffle(self) -> 'List[int]':
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.all_num)
        return self.all_num
        


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
param_2 = obj.shuffle()
param_1 = obj.reset()

print(param_2)
print(param_1)