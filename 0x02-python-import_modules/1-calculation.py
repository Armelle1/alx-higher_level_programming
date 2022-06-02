#!/usr/bin/python3
import calculator_1 as c
a = 10
b = 5
i = c.add(a, b)
m = c.sub(a, b)
n = c.mul(a, b)
o = c.div(a, b)
print("{} + {} = {}" .format(a, b, i))
print("{} + {} = {}" .format(a, b, m))
print("{} + {} = {}" .format(a, b, n))
print("{} + {} = {}" .format(a, b, o))
if __name__ == "__main__":
