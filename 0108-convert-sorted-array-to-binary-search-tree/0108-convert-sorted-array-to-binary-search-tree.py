# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None

        numlen=len(nums)//2
        
        tree=TreeNode(val=nums[numlen])
        tree.left=self.sortedArrayToBST(nums[0:numlen])
        tree.right=self.sortedArrayToBST(nums[numlen+1:])

        return tree