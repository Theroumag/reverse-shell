#!/usr/bin/python

import socket
import sys

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as e:
        print(f"Socket creation error: {str(e)}")

# Bind port and wait for client

def socket_bind():
    try:
        global host
        global port
        global s
        print(f"Binding socket to port {port}")
        s.bind((host, port))
        s.listen(5)
    except socket.error as e:
        print(f"Socket binding error: {str(e)}")
        print("Retrying...")
        socket_bind()

# Establish connection w/ client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print(f"Connection established: {address[0]}:{str(address[1])}")
    print(address)

    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input("$ ")
        if len(cmd.encode()) > 0:
            conn.send(cmd.encode("utf-8"))
            client_response = str(conn.recv(1028), "utf-8")
            print(client_response, end="")
            if cmd == "quit":
                conn.close()
                s.close()
                sys.exit()
socket_create()
socket_bind()
socket_accept()
