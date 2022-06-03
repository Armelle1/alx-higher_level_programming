#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{}" .format(n))
    if n >= 1:
        m = 0
        for i in range(n):
            m = m + int(sys.argv[i + 1])
        print("{}" .format(m))
