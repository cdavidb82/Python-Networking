#!/usr/bin/env python3

# Simple Portscanner utility

import socket

target = input("Enter IP of target: ")

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        conn = s.connect((target, port))
        return True
    except:
        return False

        for x in range(1, 501):
            if (portscan(x)):
                print("Port {} is open!".format(x))
            else:
                print("Port {} is closed!".format(x))




if __name__ == "__main__":
    portscan()