def stringRotation(A, n, p):
    return A[p+1 : n+1] + A[0 : p+1]

print(stringRotation("ABCDEFGH",8,4))