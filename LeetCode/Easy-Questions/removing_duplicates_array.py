a = []


class Solution:
    def getInputAndConvert():
        inputConsole = input()

        cleanedString = (
            inputConsole.replace("[", " ").replace("]", " ").replace(",", " ")
        )
        splittedString = cleanedString.split()

        x = 0
        for x in range(len(splittedString)):
            a.append(int(splittedString[x]))
            x += 1

    getInputAndConvert()

    print(
        "------------------------------------------------------------------------------"
    )

    def sortInArray():
        print("Array:")
        index = 0
        a.sort()

        for i in range(len(a)):
            if a[index] == a[index - 1]:
                a.remove(a[index])
            else:
                index += 1
        print(f"    Length: {len(a)}")
        print(f"    Sorted: {a}")

    sortInArray()

    print(
        "------------------------------------------------------------------------------"
    )

    def sortInSet():
        print("Set:")
        index2 = 0
        sortedArray = set()

        for index2 in range(len(a)):
            sortedArray.add(a[index2])
            index2 += 1
        print(f"    Length: {len(sortedArray)}")
        print(f"    Sorted: {sortedArray}")

    sortInSet()

    print(
        "------------------------------------------------------------------------------"
    )
