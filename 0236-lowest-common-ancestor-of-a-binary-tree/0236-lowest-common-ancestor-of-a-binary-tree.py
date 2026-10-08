# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path=[]
        q_path=[]
        
        def find(node,p,path):
            if not node:
                return False

            path.append(node)
            
            if node==p:
                return True

            if find(node.left,p,path):
                return True
                
            if find(node.right,p,path):
                return True

            path.pop()
            return False
            
        find(root,p,p_path)
        find(root,q,q_path)

        i=0
        lca=None

        while i<len(p_path) and i<len(q_path):
            if p_path[i]!=q_path[i]:
                break
            
            lca=p_path[i]
            i+=1
        
        return lca