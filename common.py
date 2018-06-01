

port = 6994

def func(arr):
    a = []
    for x in arr:
        a.append(x*x*x+x/2)
    for i in range(len(arr)):
        arr[i] = a[i] * arr[i]
    return sum(arr)
