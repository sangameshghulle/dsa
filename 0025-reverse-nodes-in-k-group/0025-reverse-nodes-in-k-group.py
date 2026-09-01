# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        current=dummy

        while True:
            group_prev=current
            group_head=current.next
            group_next=current.next
            for _ in range(k):
                if group_next is None:
                    return dummy.next
                group_next=group_next.next
            
            prev=group_next
            curr=group_head
            
            # while curr != group_next:
            for _ in range(k):
                nxt=curr.next
                curr.next=prev
                prev,curr=curr,nxt
            
            group_prev.next=prev

            current=group_head