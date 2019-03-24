while True:
    try:
        data = input()
        result = []
        for i in data:
            if i not in result:
                result.append(i)
        print(''.join(result))
    except:
        break