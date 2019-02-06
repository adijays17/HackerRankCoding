def checkPossibility(A):
    def monotone_increasing(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                return False
        return True
    new = A[:]
    for i in range(len(A)):
        old_ai = A[i]
        new[i] = new[i-1] if i > 0 else float('-inf')
        if monotone_increasing(new):
            return True
        new[i] = old_ai

        return False

print(checkPossibility([2,3,3,2,4]))