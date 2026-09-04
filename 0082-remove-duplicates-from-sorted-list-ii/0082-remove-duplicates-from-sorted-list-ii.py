# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0,head)
        node=dummy.next
        prev=dummy
        while node and node.next is not None:
            if node.next is not None and node.val==node.next.val:
                while node.next is not None and node.val==node.next.val:
                    node=node.next
                prev.next=node.next
            else:
                prev=prev.next
            node=node.next
        return dummy.next
