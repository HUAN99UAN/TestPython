
def rotateString(A, n, p):
    return A[p+1 : n] + A[0 : p+1]
print(rotateString("ABCDEFGH",8,4))