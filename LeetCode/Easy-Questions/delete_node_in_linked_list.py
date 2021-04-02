head = [-3, 5, -99]
node = -3


class Solution:
    @staticmethod
    def deleteNodeInLinkedList():
        index = 0
        for i in range(len(head)):
            if head[index] == node:
                head.remove(head[index])
                print(head)
                break
            else:
                index += 1

    deleteNodeInLinkedList()