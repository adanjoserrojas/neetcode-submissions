# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set ()
        current = head

        while current is not None:
            if current.val not in seen:
                seen.add(current.val)
            elif current.val in seen and current.next is not None:
                return True
            current = current.next

        return False