import threading
import time
import random
import socket as mysoc
import client as myclient

def toAscii(words):
    asciiWords = []
    for word in words:
        asciiString = ""
        for y in range(0, len(word)-1):
            asciiString += (str(ord(word[y])) + "_")
        asciiString += str(ord(word[len(word)-1]))
        asciiWords.append(asciiString)
    return " ".join(asciiWords)

def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',50043)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)

    words = csockid.recv(4096).decode('utf-8').split(" ")
    print("[S]: Message received:: ", words)
    asciiWords = toAscii(words)
    csockid.send(asciiWords.encode('utf-8'))

    ss.close()
    exit()


def main():
    t1 = threading.Thread(name='server', target=server)
    t1.start()
    time.sleep(random.random()*5)
    t2 = threading.Thread(name='client', target=myclient.client)
    t2.start()

if __name__ == "__main__":
    main()



