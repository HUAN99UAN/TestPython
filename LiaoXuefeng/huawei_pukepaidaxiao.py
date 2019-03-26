card_dict = {'3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'J':9, 'Q':10, 'K':11, 'A':12, '2':13, 'joker':14, 'JOKER':15}
while True:
    try:
        card_1, card_2 = input().split('-')
        if card_1 == 'joker JOKER' or card_2 == 'joker JOKER': # 王炸
            print('joker JOKER')
        else:
            card_1 = list(card_1.split())
            card_2 = list(card_2.split())
            len1 = len(card_1)
            len2 = len(card_2)
            if len1 == len2: # 同类比较
                if card_dict[card_1[0]] > card_dict[card_2[0]]:
                    print(' '.join(card_1))
                else:
                    print(' '.join(card_2))
            else: # 不等，炸大于其他；或者就是无法比较！
                if len1 == 4:
                    print(' '.join(card_1))
                elif len2 == 4:
                    print(' '.join(card_2))
                else:
                    print('ERROR')
    except:
        break