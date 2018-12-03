#!/usr/bin/python3


def is_leapyear(y: int) -> None:
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


y = int(input())
print(is_leapyear(y))
