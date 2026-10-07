# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val)
        
        if root.left and root.val>val:
            self.insertIntoBST(root.left,val)
            
        if root.right and root.val<val:
            self.insertIntoBST(root.right,val)
        
        if not root.left and root.val>val:
            root.left=self.insertIntoBST(root.left,val)
        
        if not root.right and root.val<val:
            root.right=self.insertIntoBST(root.right,val)

        return root