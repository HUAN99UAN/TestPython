import collections

record = collections.OrderedDict() #  这个类型在添加键的时候会保持顺序,因此键的迭代总是一致的
while True:
    try:
        name_num = input().split('\\')[-1] # E:\V1R2\product\fpgadrive.c 1325 ——> fpgadrive.c 1325;strip: 用来去除头尾字符、空白符
        if name_num in record:
            record[name_num] = record[name_num] + 1
        else:
            record[name_num] = 1
    except:
        break

lstTuple = sorted(record.items(), key = lambda d:d[1], reverse=True) # 根据value倒序排序，.items()使返回的值还是字典

count = 0
for key in lstTuple:
    if count > 7:
        break
    count += 1
    if len(key[0].split()[0]) > 16:
        print(key[0].split()[0][-16:], key[0].split()[1], key[1])
    else:
        print(key[0].split()[0], key[0].split()[1], key[1])

