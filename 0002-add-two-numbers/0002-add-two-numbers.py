# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0)
        node=dummy
        while l1 is not None or l2 is not None:
            l1val=l1.val if l1 is not None else 0
            l2val=l2.val if l2 is not None else 0
            ans=carry+l1val+l2val
            carry=ans//10
            node.next=ListNode(ans%10)
            node=node.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next

        while carry!=0:
            node.next=ListNode(carry%10)
            carry=carry//10
            node=node.next

        return dummy.next
