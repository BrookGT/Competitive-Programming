# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        current = head
        
        while current and current.next:
            gcd_value = gcd(current.val, current.next.val)

            gcd_node = ListNode(gcd_value)

            gcd_node.next = current.next
            current.next = gcd_node

            current = gcd_node.next
        
        return head
