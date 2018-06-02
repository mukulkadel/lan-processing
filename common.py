import math
import multiprocessing as mp

port = 6994

def func(arr):
    part = mp.cpu_count()
    print("CPU count: {}".format(part))

    q = mp.Queue()
    l = len(arr)
    ps = [mp.Process(target=task,args=(arr[(l*i//part):(l*(i+1)//part)],q)) for i in range(part)]

    for i in range(part):
        ps[i].start()

    for i in range(part):
        ps[i].join()

    s = 0
    for i in range(q.qsize()):
        s += q.get()

    return s

def task(arr,q):
    arr = list(arr)
    a = []
    for x in arr:
        a.append(math.sqrt(x*x*x+x*x+x/2))
    for i in range(len(arr)):
        arr[i] = a[i] * arr[i]

    q.put(sum(arr))
    return
