# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        second=slow.next
        slow.next=None
        
        while second:
            nextNode=second.next
            second.next=prev
            prev=second
            second=nextNode
        
        # ans=head
         
        # print("before:",head)
        while prev and head:
            headNode=head.next
            prevNode=prev.next
            head.next=prev
            prev.next=headNode
            prev=prevNode
            head=headNode
        # print("after:",ans)
            
        