def checkIfPalindrome(s):
    if s == s[::-1]:
        return True
    return False

def split(s, c):
    temp = s.split(c)
    print(temp)

def wthoutSplit(s, c):
     while c in s:
             s = s.lstrip(s.index(c)
             print(s)
             
def crash():
    print("1")
    print("2")


wthoutSplit("Aditiya", 'i')