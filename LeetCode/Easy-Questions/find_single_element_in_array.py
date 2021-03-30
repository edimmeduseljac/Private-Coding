nums = []

class Solution:
    def getNumbers():
        inputConsole = input("Enter the numbers to check: ")

        cleanedString = inputConsole.replace("[", " ").replace("]", " ").replace(",", " ")
        splittedString = cleanedString.split()
        
        x = 0
        for x in range(len(splittedString)): 
            nums.append(int(splittedString[x]))
            x+=1
            
    getNumbers()
    
    def findSingleNumber():
        index = 0
        for i in range(len(nums)):
            if len(nums) > 1:
                if nums[index] == nums[index - 1]:
                    nums.remove(nums[index])
                    nums.remove(nums[index-1])
                index +=1
        print(nums[0])
    findSingleNumber()
    '''
    def findSingleNumberAlternative():
        index = 0
        for i in range(len(nums)):
            if nums.count(nums[index]) > 1:
                count = nums.count(nums[index])
                for i in range(count):
                    nums.remove(nums.index(nums[index]))
            else:
                index += 1
        print(nums)
    findSingleNumberAlternative()
    '''