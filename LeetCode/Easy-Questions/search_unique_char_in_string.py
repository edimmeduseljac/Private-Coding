s = "aabbccd"

checkingArray = []
index = 0
for i in s:
    if len(checkingArray) == len(s) and checkingArray[index] != i:
        checkingArray.clear()
    else:
        checkingArray.append(i)
        index += 1

index = 0
v = 1
unique = ""
for i in range(len(checkingArray)):
    if checkingArray.count(checkingArray[index]) > 1:
        if index < len(checkingArray) - 1:
            index += 1
        else:
            print(f"return {-1}")
            break
    elif checkingArray.count(checkingArray[index]) == 1:
        unique = checkingArray[index]
        print(f"return {checkingArray.index(checkingArray[index])}")
        break
