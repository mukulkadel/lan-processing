import math

port = 6994

def func(arr):
    arr = list(arr)
    a = []
    for x in arr:
        a.append(math.sqrt(x*x*x+x*x+x/2))
    for i in range(len(arr)):
        arr[i] = a[i] * arr[i]
    return sum(arr)
