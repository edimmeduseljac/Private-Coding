nums1 = [2, 1, 2, 1, 2, 1, 2, 1]
nums2 = [1, 2]
output = []

indexNums1 = 0
indexNums2 = 0
indexOutput = 0


class Solution:
    @staticmethod
    def findIntersection():

        global indexNums1
        global indexNums2
        global indexOutput

        if len(nums1) > len(nums2):
            for i in range(len(nums1)):
                if indexNums2 == len(nums2):
                    indexNums2 = 0
                elif nums1[indexNums1] == nums2[indexNums2]:
                    if len(output) > 0:
                        indexOutput = 0
                        if nums1[indexNums1] in output:
                            indexNums2 += 1
                            indexNums1 += 1
                        else:
                            output.append(nums1[indexNums1])
                    else:
                        output.append(nums1[indexNums1])
                        indexNums2 += 1
                        indexNums1 += 1
                else:
                    indexNums1 += 1
        else:
            for i in range(len(nums2)):
                if indexNums1 == len(nums1):
                    indexNums1 = 0
                elif nums1[indexNums1] == nums2[indexNums2]:
                    if len(output) > 0:
                        indexOutput = 0
                        if nums2[indexNums2] in output:
                            indexNums2 += 1
                            indexNums1 += 1
                        else:
                            output.append(nums2[indexNums2])
                    else:
                        output.append(nums2[indexNums2])
                        indexNums2 += 1
                        indexNums1 += 1
                else:
                    indexNums2 += 1
        print(output)

    findIntersection()