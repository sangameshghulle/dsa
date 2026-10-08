# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node,l,h):
            if not node:
                return True
            
            if l>=node.val or node.val>=h:
                return False
            
            return dfs(node.left,l,node.val) and dfs(node.right,node.val,h)
            
        return dfs(root,-float('inf'),float('inf'))