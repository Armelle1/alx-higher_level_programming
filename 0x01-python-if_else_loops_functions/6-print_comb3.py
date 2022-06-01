#!/usr/bin/python3
for i in range(0, 89):
    value = 10 * (i % 10) + i // 10
    if i < value and i % 11 != 0:
        print("{:02d}, " .format(i), end="")
print("{:02d}" .format(89))
