# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        _headA = headA
        len_headA = 0
        while (_headA is not None):
            _headA = _headA.next
            len_headA += 1

        _headB = headB
        len_headB = 0
        while (_headB is not None):
            _headB = _headB.next
            len_headB += 1

        dis = abs(len_headB - len_headA)
        if len_headB > len_headA:
            rem = len_headB - dis
            for i in range(dis):
                headB = headB.next
        else:
            rem = len_headA - dis
            for i in range(dis):
                headA = headA.next

        for i in range(rem):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
