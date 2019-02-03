# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
        while (curr_node != None) and (curr_node.next != None):
            if curr_node.val == curr_node.next.val:
            
                
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
                
                
        
        return head

s=Solution()
print(s.deleteDuplicates([1,1,2]))


