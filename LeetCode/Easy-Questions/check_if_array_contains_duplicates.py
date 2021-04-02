nums = []


class Solution:
    @staticmethod
    def getNumbers():
        inputConsole = input("Enter the numbers to check: ")

        cleanedString = (
            inputConsole.replace("[", " ").replace("]", " ").replace(",", " ")
        )
        splittedString = cleanedString.split()

        x = 0
        for x in range(len(splittedString)):
            nums.append(int(splittedString[x]))
            x += 1

    getNumbers()

    @staticmethod
    def checkIfDuplicates():
        index = 0
        v = 1
        duplicate = 0
        for i in range(len(nums)):
            if v < len(nums):
                if nums[index] == nums[index - v]:
                    duplicate = 1
                else:
                    v += 1
        if duplicate == 1:
            print("true")
        else:
            print("false")

    checkIfDuplicates()