import socket as mysoc
import time
import random

# Strategy: First send server the length of the array
# Server Will loop through recv the correct number of times
def readFile(fileName):
    testFile = open('HW1test.txt', 'r')
    text = testFile.read()
    testFile.close()
    words = " ".join(text.split("\n"))
    return words

def writeFile(asciiWords):
    f = open("HW1out.txt", "w")

    for x in range(0, len(asciiWords)-1):
        f.write(asciiWords[x] + "\n")
    f.write(asciiWords[len(asciiWords)-1])

    f.close()


#client task
def client():
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        cs.settimeout(0.5)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))


# Define the port on which you want to connect to the server
    port = 50043
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
# connect to the server on local machine
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)

    words = readFile('HW1test.txt')
    cs.send(words.encode('utf-8'))
    asciiMsg = cs.recv(4096).decode('utf-8').split(" ")
    print("[C]: Message received:: ", asciiMsg)

    writeFile(asciiMsg)
    print("[C]: ASCII words now written in file: HW1out.txt")

# close the cclient socket
    cs.close()
    exit()