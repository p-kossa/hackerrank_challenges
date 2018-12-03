#!/bin/python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

a.sort()
record = a[n-1] - a[0]

for i in range(n-1):
    if (a[i+1] - a[i]) < record:
        record = a[i+1] - a[i]

print(record)