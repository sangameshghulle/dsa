# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         dummy=ListNode(0,head)
#         prev=dummy
#         curr=head
#         while curr and curr.val!=x:
#             prev=prev.next
#             curr=curr.next
#         if not curr:
#             return head
#         found=curr
#         prevlast=prev
#         prevlast.next=None
#         prevcurr=dummy

#         while curr and curr.next:
#             if curr.next.val<x:
#                 prevcurr=dummy
#                 while prevcurr.next and prevcurr.next.val<=curr.next.val:
#                     prevcurr=prevcurr.next
#                 prevnxtnode=prevcurr.next
#                 prevcurr.next=curr.next
#                 prevcurr.next.next=prevnxtnode
#                 if not prevnxtnode:
#                     prevlast=curr.next

#                 curr.next=curr.next.next

#             else:
#                 curr=curr.next

#         prevlast.next=found

#         return dummy.next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = curr
            else:
                greater.next = curr
                greater = curr

            curr = curr.next

        greater.next = None
        less.next = greater_dummy.next

        return less_dummy.next