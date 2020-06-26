class CQueue(object):
    def __init__(self):
        self.quene = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.quene.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.quene == []:
            return -1
        head = self.quene[0]
        self.quene = self.quene[1:]
        return head


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()