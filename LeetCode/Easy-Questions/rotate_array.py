nums = []
k = 0


class Solution:
    def getNumbers():
        inputConsole = input("Enter the numbers you want to rotate: ")

        cleanedString = (
            inputConsole.replace("[", " ").replace("]", " ").replace(",", " ")
        )
        splittedString = cleanedString.split()

        x = 0
        for x in range(len(splittedString)):
            nums.append(int(splittedString[x]))
            x += 1

    getNumbers()

    def getRotateCount():
        inputConsole = int(
            input("Enter the number of times you want to rotate the entered numbers: ")
        )
        global k
        k = inputConsole

    getRotateCount()

    def rotateArray():
        x = 0
        while x < k:
            index = 0
            for i in range(len(nums)):
                nums.append(nums[index - 1])
                index += 1
            halfLength = int(len(nums) / 2)
            for i in range(halfLength):
                nums.remove(nums[0])
            x += 1
        print(nums)

    rotateArray()