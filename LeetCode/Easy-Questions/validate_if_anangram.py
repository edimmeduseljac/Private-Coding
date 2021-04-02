s = "nagaram"
t = "nagaram"


class Solution:
    @staticmethod
    def validateAnangram():
        if len(s) == len(t):
            if sorted(s) == sorted(t):
                print("true")
            else:
                print("false")
        else:
            print("false")

    validateAnangram()