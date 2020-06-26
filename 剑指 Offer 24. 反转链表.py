# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while (head is not None):
            cur_node = ListNode()
            cur_node.val = head.val
            cur_node.next = new_head
            head = head.next
            new_head = cur_node

        return new_head
