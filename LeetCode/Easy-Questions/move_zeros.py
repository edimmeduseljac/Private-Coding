nums = []

class Solution:

    global nums

    def getNumbers():
            inputConsole = input("Enter the numbers to check: ")

            cleanedString = inputConsole.replace("[", " ").replace("]", " ").replace(",", " ")
            splittedString = cleanedString.split()
            
            x = 0
            for x in range(len(splittedString)): 
                nums.append(int(splittedString[x]))
                x+=1
    getNumbers()

    def move_zeros():
        index = 0
        for i in range(len(nums)):
            if nums[index] == 0:
                nums.append(nums[index])
                nums.remove(nums[index])
                index += 1
            else: 
                index += 1
        print(nums)
    move_zeros()
