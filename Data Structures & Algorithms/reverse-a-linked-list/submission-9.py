# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev = None

        while current is not None:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        
        head = prev

        return head
        