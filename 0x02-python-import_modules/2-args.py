#!/usr/bin/python3
import sys
import argparse
parser = argparse.ArgumentParser()
args = parser.parse_args()
n = len(sys.argv) - 1
i = 1
if i == 1:
    print(n, "arguments.\n")
elif i > 1:
    for i in range(n):
        print("{} arguments:" .format(n))
        print("{}: {}" .format(i, args))
