# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        head = result
        while (l1 is not None or l2 is not None):
            if l1 is None:
                result.next = l2
                break
            elif l2 is None:
                result.next = l1
                break

            if l1.val < l2.val:
                result.next = ListNode(l1.val)
                result = result.next
                l1 = l1.next
            else:
                result.next = ListNode(l2.val)
                result = result.next
                l2 = l2.next

        return head.next
