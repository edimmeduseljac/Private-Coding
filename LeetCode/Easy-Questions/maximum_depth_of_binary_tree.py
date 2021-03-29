root = [3, 9, 20, None, None, 15, 7]


class Solution:
    def maximumDepthBinaryTree():
        index = 1
        maximum_depth = 0
        if len(root) == 0:
            maximum_depth = 0
        else:
            maximum_depth = 1
            for i in range(len(root) - 1):
                if index == len(root):
                    break
                elif (
                    root[index] != None
                    and root[index + 1] != None
                    or root[index] == None
                    and root[index + 1] != None
                    or root[index] != None
                    and root[index + 1] == None
                ):
                    maximum_depth += 1
                    index += 2
                else:
                    index += 2
        print(maximum_depth)

    maximumDepthBinaryTree()