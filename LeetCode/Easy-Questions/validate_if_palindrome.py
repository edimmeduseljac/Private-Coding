s = "A man, a plan, a canal: Panama"


class Solution:
    def validatePalindrome():
        cleanedS = s.replace(",", "").replace(" ", "").replace(":", "").lower()
        reversedCleanedS = cleanedS[::-1]

        if cleanedS == reversedCleanedS:
            print("true")
        else:
            print("false")

    validatePalindrome()