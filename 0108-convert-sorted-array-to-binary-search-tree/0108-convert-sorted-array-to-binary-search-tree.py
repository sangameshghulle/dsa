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

        # numlen=len(nums)//2
        
        # tree=TreeNode(val=nums[numlen])
        # tree.left=self.sortedArrayToBST(nums[0:numlen])
        # tree.right=self.sortedArrayToBST(nums[numlen+1:])

        def helper(nums,l,r):
            if l>r:
                return None

            mid=(l+r+1)//2
            tree=TreeNode(val=nums[mid])

            tree.left=helper(nums,l,mid-1)
            tree.right=helper(nums,mid+1,r)

            return tree

        return helper(nums,0,len(nums)-1)