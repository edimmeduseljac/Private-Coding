s = ["h","e","l","l","o"]

#Einfachste Variante: 
#s.reverse()

def reverseString():
    index = 0
    v = 1
    index = len(s) - 1
    for i in range(len(s)):
        s.append(s[index])
        index -= 1

    index2 = 0
    for i in range(int(len(s)/2)):
        s.remove(s[index2])
        index2 += 1
    print(s)