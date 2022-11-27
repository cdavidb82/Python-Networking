#!/usr/bin/env python3

# This is a  script for creating a quick HTTP server using python
# This script is just to get a working knowledge on how socket is used to access
# network utilities

# Python3 has a module preinstalled that does the same
# using "python3 -m http.server <port>"

import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind("127.0.0.1", 9999)
    s.listen()

    print("Listening on Port 9999......")



if __name__ == "__main__":
    main()
