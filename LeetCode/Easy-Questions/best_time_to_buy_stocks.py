def getInputAndConvert():
        inputConsole = input()

        cleanedString = inputConsole.replace("[", " ").replace("]", " ").replace(",", " ")
        splittedString = cleanedString.split()
        
        x = 0
        for x in range(len(splittedString)): 
            a.append(int(splittedString[x]))
            x+=1

#getInputAndConvert()

prices = [7,1,5,3,6,4]

def maxProfit():
    profit = 0
    for i in range(1, len(prices)):
        profit += max(prices[i]-prices[i-1], 0)
    print(profit)

maxProfit()