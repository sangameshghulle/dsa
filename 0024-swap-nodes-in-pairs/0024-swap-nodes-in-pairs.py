# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        node=dummy
        while node.next and node.next.next:
            node1=node.next
            node2=node.next.next
            node3=node.next.next.next
            node.next=node2
            node.next.next=node1
            node.next.next.next=node3
            node=node1
        
        return dummy.next