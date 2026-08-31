# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        count=0
        node=head
        while node:
            node=node.next
            count+=1
        k=k%count 
        for _ in range(k):
            end=head
            while end.next and end.next.next:
                end=end.next
            node=end.next
            end.next=None
            node.next=head
            head=node
        return head