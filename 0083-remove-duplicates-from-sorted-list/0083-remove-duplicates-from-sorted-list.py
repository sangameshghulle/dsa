# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        seen=set()
        curr=dummy
        while curr.next:
            if curr.next.val in seen:
                curr.next=curr.next.next

            else:
                seen.add(curr.next.val)

                curr=curr.next
        
        return dummy.next