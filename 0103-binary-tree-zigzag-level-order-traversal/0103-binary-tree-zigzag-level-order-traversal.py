# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        q=deque([root])
        res=[]

        reverse=False

        while q:
            lvl=[]
            llen=len(q)
            for _ in range(llen):
                node=q.popleft()
                lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                lvl=lvl[::-1]
            reverse=not reverse
            res.append(lvl)
        
        return res