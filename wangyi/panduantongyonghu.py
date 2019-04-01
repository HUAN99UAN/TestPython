import collections
count1 = collections.OrderedDict()
device1 = collections.OrderedDict()
while True:
    try:
        num, account = input().split()
        print(account)
        num = int(num)
        account1 = []
        device =[] #
        for i in range(num):
            account2, device2, time2 = input().split()[2:5]
            device.append(device2) #
            print(account2, device2, time2)
            if time2 >= 60:
                if (account2 not in account1) or (device2 not in device1):
                    account1.append(account2)
                    device1[account2] = device2
                    count1[account2] = 1
                elif (account2 in account1) and (device2 in device1):
                    count1[account2] += 1
        for i in range(len(account1)):
            if account1[i] == account and count1[account1[i]] >=3: #
                device.append(device1[account1[i]]) #
            if account1[i] != account and (device1[account1[i]] in device) and count1[account1[i]] >=3: #
                print(account1[i])

        print(count1)
    except:
        break
