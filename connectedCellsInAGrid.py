#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def connectedCell(matrix):
    def floodfill(i,j):
        if i>=n or j>=m or matrix[i][j]==-1 or matrix[i][j]==0 or i<0 or j<0:
            return 0
        else:
            matrix[i][j]=-1
            return 1+(floodfill(i+1,j)+floodfill(i-1,j)+floodfill(i,j+1)+floodfill(i,j-1)+floodfill(i+1,j-1)+floodfill(i+1,j+1)+floodfill(i-1,j-1)+floodfill(i-1,j+1))

    res=-999

    for i in range(n):
        for j in range(m):
            res=max(res,floodfill(i,j))
    return(res) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
