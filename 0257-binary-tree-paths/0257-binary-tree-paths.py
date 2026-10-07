# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []
        result=[]
        def paths(node,path):
            if not node:
                return
            
            path+=f'->{node.val}'

            if not node.left and not node.right:
                result.append(path)
            
            paths(node.left,path)
            paths(node.right,path)
        
        paths(root.left,f"{root.val}")
        paths(root.right,f"{root.val}")

        if not result:
            result.append(f"{root.val}")

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna