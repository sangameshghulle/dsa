# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=dummy
        for _ in range(left-1):
            slow=slow.next
        
        prev=None
        current=slow.next
        for _ in range(right-left+1):
            next=current.next
            current.next=prev
            prev=current
            current=next
        slow.next.next = current
        slow.next = prev

        # print(dummy)

        return dummy.next