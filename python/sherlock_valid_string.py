#!/bin/python3


def isValid(s) -> str:
    freq = dict()
    
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    count = int()

    for k, v in freq.items():
        if v > 2:
            return("NO")
        if v == 2:
            count += 1
            if count > 1:
                return("NO")
    
    return("YES")


if __name__ == '__main__':
    s = input()

    result = isValid(s)
    print(result)
