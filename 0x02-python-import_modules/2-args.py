#!/usr/bin/python3
import sys
n = len(sys.argv) - 1
if n == 0:
    print(n, "arguments.")
if n == 1:
    print("{} argument:" .format(n))
    print("{}: {}" .format(n, sys.argv[n]))
if n > 1:
    print("{} arguments:" .format(n))
    for i in range(n):
        print("{}: {}" .format((i + 1), sys.argv[i + 1]))
