import socket
import time
import array

slave_ip = "192.168.43.49"
port = 6994

def get_data(s):
    data = []
    l = int(s.recv(40))
    while True:
        if l <= 0:
            break
        elif l > 512:
            tmp = s.recv(512)
        else:
            tmp = s.recv(l)
        data.append(tmp)
        l -= len(tmp)

    tmp = b"".join(data)
    data = tmp.decode()
    return float(data)

def get_result(arr):
    arr = array.array('l',arr)
    s = socket.socket()
    s.connect((slave_ip,port))
    tmp = arr.tobytes()
    l_tmp = str(len(tmp))
    s.send(("0"*(40-len(l_tmp))+l_tmp).encode())
    s.send(tmp)
    result = get_data(s)
    s.close()
    return result

if __name__=="__main__":
    arr = list(range(100000))

    #for verification
    old_t = time.time()
    print("Master result: {}".format(sum(arr)))
    new_t = time.time()
    print("Normal way, took: {}".format(new_t-old_t))

    #calling slaves to process data
    old_t = time.time()
    print("Network result: {}".format(get_result(arr)))
    new_t = time.time()
    print("Over network, took: {}".format(new_t - old_t))
