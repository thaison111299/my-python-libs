#!/bin/python3

import os
import sys

# Complete the solve function below.

def detNum(a, b, x):
    b = abs(b)
    for i in range(1, x+1):   
        if (i*a)%x == b:
            return i 
    return -1



def solve(a, b, x):
    if b<0:
        z = detNum(a, b, x)
        return z%x 
    
    if b%2==0:
        b//=2
        return ((a**b)*(a**b))%x
    b//=2
    return ((a**b)*(a**b)*a)%x
def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = solve(a, b, x)

        # fptr.write()
        print(str(result) + '\n')

    # fptr.close()

main()