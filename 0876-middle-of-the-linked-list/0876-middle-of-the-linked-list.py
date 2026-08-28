# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[head]
        curr=head.next
        while curr:
            nodes.append(curr)
            curr=curr.next
        n=len(nodes)
        return nodes[n//2]