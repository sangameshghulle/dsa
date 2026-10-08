# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return None
        
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left or not root.right:
                if root.left:
                    return root.left
                elif root.right:
                    return root.right
            successor=root.right
            while successor.left:
                successor=successor.left
            root.val=successor.val
            root.right=self.deleteNode(root.right,successor.val)
        return root