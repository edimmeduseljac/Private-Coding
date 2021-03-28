#Reverse Integer question

x = int(input("Enter the number you want to reverse: "))

class Solution:
    def reverseInteger():
        v = 0
        number = 0
        if x > 0: 
            a = str(x)
            for i in a: 
                number = number + int(i) * pow(10,v)
                v += 1
        else: 
            n = x - (2*x)
            a = str(n)
            for i in a: 
                number = number + int(i) * pow(10,v) * (-1)
                v += 1
        print(number)
    reverseInteger()