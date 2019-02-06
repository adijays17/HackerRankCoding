def flipSign(s,K):
    def countSetBits(n): 
        count = 0
        while n: 
            count += n & 1
            n >>= 1
        return count 
        
    def FlippedCount(a , b): 
        return countSetBits(a^b) 
    a = "+++---++"
    b = "---+++--"
    print(FlippedCount(a, b)) 

flipSign("+++",2)