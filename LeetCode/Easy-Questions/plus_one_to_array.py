digits = []


class Solution:

    global digits

    @staticmethod
    def getNumbers():
        inputConsole = input("Enter the numbers to check: ")

        cleanedString = (
            inputConsole.replace("[", " ").replace("]", " ").replace(",", " ")
        )
        splittedString = cleanedString.split()

        x = 0
        for x in range(len(splittedString)):
            digits.append(int(splittedString[x]))
            x += 1

    getNumbers()

    @staticmethod
    def addOneToNumber():
        index = 0
        number = 0
        output = []
        count = len(digits) - 1

        for i in range(len(digits)):
            exponent = count - index
            number = number + digits[index] * pow(10, exponent)
            index += 1
        finalnumber = number + 1

        for element in str(finalnumber):
            output.append(int(element))
        print(output)

    addOneToNumber()