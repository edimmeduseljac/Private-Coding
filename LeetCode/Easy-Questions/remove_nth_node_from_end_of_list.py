head = [1, 2]
n = 1


class Solution:
    @staticmethod
    def removeNodeFromEndOfList():
        head.remove(head[len(head) - n])
        print(head)

    removeNodeFromEndOfList()