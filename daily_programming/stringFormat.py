def stringFormat(A, n, arg):
    while "%s" in A and len(arg) > 0:
        A = A.replace("%s", arg.pop(0), 1)# ython replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，
                                          # 如果指定第三个参数max，则替换不超过 max 次。
    return A + ''.join(arg)

print(stringFormat("A%sC%sE",7,['B','D','F']))