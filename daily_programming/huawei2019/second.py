import re

def main():
    validStrs = []
    invalidStrs = []

    while True:
        text = input()
        if text is '':
            break
        m = re.compile(r'^[0-9a-zA-Z]+$').match(text)
        if m is None:
            invalidStrs.append(text)
        elif not text in validStrs:
            validStrs.append(text)
        for valid in validStrs:
            print(valid, end='')
        print('')
        for invalid in invalidStrs:
            print(invalid, end='')
        print('')
        output3 = []
        for valid in validStrs:
            l = len(valid)
            if l > 10:
                valid = valid[10:]+valid[:10]
            else:
                valid = valid[10%l:]+valid[:10%l]
            print(valid, end='')
            output3.append(valid)
        output3.sort()
        for out in output3:
            print(out, end='')

if __name__== "__main__" :
    main()