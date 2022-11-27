#!/usr/bin/env python3

# This is a quick script for creating a quick HTTP server using python

import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind("127.0.0.1", 9999)
    s.listen()

    print("Listening on Port 9999......")



if __name__ == "__main__":
    main()
