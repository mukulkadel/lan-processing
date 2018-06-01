import socket
import array


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
    data = array.array('l',[])
    data.frombytes(tmp)
    return data.tolist()

def func(data):
    s = sum(data)
    return s

if __name__ == "__main__":
    s = socket.socket()
    s.connect(("8.8.8.8",53))
    slave_ip = s.getsockname()[0]

    s.bind((slave_ip,port))
    s.listen(5)
    print("Ready to serve master.")

    while True:
        c,addr = s.accept()
        print("Connected with master {}".format(addr))
        data = get_data(c)
        print("Data received")
        result = str(func(data))
        tmp = result.encode()
        l_tmp = str(len(tmp))
        c.send(("0"*(40-len(l_tmp))+l_tmp).encode())
        c.send(tmp)
        c.close()
        print("done.")
        break
    s.close()
