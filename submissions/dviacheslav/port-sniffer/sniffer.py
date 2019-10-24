#! /usr/bin/python3.6

import sys
import socket
import argparse

parser = argparse.ArgumentParser(description="TCP sniffer search opened ports in particular host")
parser.add_argument("--host", type=str, required=True, metavar="host", help="host name, example: www.google.com")
parser.add_argument("--ports", type=str, metavar="ports", default="0-65535", help="range ports, example: 24-350")
args = parser.parse_args()

min_port = int(args.ports.split("-")[0])
max_port = int(args.ports.split("-")[1])

if min_port < 0 or min_port > 65535 or max_port < 0 or max_port > 65535:
    print("port index must be in range 0-65535")
    exit(1)

if min_port > max_port:
    min_port, max_port = max_port, min_port

def scanPorts(host, start, end):
    open_ports = []
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        success = s.connect_ex((host, port))
        if success == 0:
            open_ports.append(port)
            print(".", end="")
            sys.stdout.flush()
        s.close()
    print("\n")
    return open_ports

ports = scanPorts(args.host, min_port, max_port)

if len(ports) == 0:
    print("Not found opened ports in range {}-{}".format(min_port, max_port))
elif len(ports) == 1:
    print("{} port is open".format(ports[0]))
else:
    print(",".join(map(str, ports)) + " ports are opened")
exit(0)



