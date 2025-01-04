# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        part_size = length // k
        extra_parts = length % k
        
        result = []
        current = head
        
        for i in range(k):
            part_head = current
            current_part_size = part_size + (1 if i < extra_parts else 0)
            
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
            
            if current:
                next_part_head = current.next
                current.next = None
                current = next_part_head
            
            result.append(part_head)
        
        return result
            
