# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        
        result=[]

        def findpath(node,rem,path):

            if not node:
                return

            rem-=node.val
            path.append(node.val)

            if not node.left and not node.right and rem==0:
                result.append(path.copy())
            findpath(node.left,rem,path)
            findpath(node.right,rem,path)
            path.pop()
        
        findpath(root,targetSum,[])
        return result