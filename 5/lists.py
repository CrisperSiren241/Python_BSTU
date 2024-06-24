import random

def randomList(n):
    return [random.randint(-99, 99) for _ in range(n)]

def randomMatrix(n):
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]

def maxLength(X):
    return max(X, key=len)

def currentSums(X):
    current_sum = 0
    sums = []
    for num in X:
        current_sum += num
        sums.append(current_sum)
    return sums

def threeSimbol(S):
    return [S[i:i+3] for i in range(0, len(S)-2)]


