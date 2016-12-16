#!/usr/bin/python
import sys
x = sys.argv[1]
y = sys.argv[2]
if len(sys.argv) >= 2:
    print(int(sys.argv[1]) + int(sys.argv[2]))
else:
    print("usage: python3 solution.py 0P1 0P2")
