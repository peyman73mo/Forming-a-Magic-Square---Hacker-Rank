import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    a = [[], [], []]
    b = [[], [], []]

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and i != k and j != k:
                    if i + j + k == 15:
                        if j == 5:
                            a[1].append([i, j, k])
                        elif (i % 2 == 0 or k % 2 == 0) and (j % 2 != 0 and j != 5):
                            a[0].append([i, j, k])
                            a[2].append([i, j, k])

    for i in a[0]:
        for j in a[1]:
            for k in a[2]:
                if (i[0] + j[0] + k[0] == 15) and (i[0] + j[1] + k[2] == 15) and (i[2] + j[2] + k[2] == 15):
                    b[0].append(i)
                    b[1].append(j)
                    b[2].append(k)


    k = 100
    j_ = -1
    for m in range(8):
        temp = 0
        for i in range(len(b)):
            for j in range(len(b)):
                # print(b[i][m][j])
                temp += abs(b[i][m][j] - s[i][j])
        if temp < k:
            j_ = m
            k = temp
    return k


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
