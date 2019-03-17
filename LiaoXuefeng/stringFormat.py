def stringFormat(A, n, arg):
    while "%s" in A and len(arg) > 0:
        A = A.replace("%s", arg.pop(0), 1)
    return A + ''.join(arg)

print(stringFormat("A%sC%sE",7,['B','D','F']))