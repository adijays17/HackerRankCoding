class Solution:
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        sum = sum - root.val
        if root.left == None and root.right == None:
            if sum == 0:
                return True
            else:
                return False

        if self.hasPathSum(root.left, sum):
            return True
        if self.hasPathSum(root.right, sum):
            return True
        return False

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t = TreeNode(1)
t.left = TreeNode(2)
s = Solution()
print(s.hasPathSum(t, 1))