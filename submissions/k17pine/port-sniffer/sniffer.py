import socket
import sys
from argparse import ArgumentParser


def is_ip(arg):
    try:
        result = socket.gethostbyname(arg)
        return result
    except (socket.error, TypeError):
        sys.stdout.write("You must input right ip/host address")
        sys.exit(1)


def is_port(arg):
    try:
        ports = arg.split("-", 1)
        minn = int(ports[0])
        maxi = int(ports[1])
        if (minn >= 0) and (minn < 65536):
            if (maxi >= 0) and (maxi < 65536):
                return minn, maxi
    except (TypeError, ValueError):
        sys.stdout.write("You must input right port number in format <start_port>-<end_port>")
        sys.exit(1)


def main():
    socket.setdefaulttimeout(0.3)
    min_port = 0
    max_port = 65535
    opened = []
    parser = ArgumentParser()
    parser.add_argument("-p", "--ports", dest="ports",
                        help="Two ports in range 0-65535")
    parser.add_argument("--host", dest="ip",
                        help="IP address or domain name")
    args = parser.parse_args()
    host_ip = is_ip(args.ip)
    if args.ports is not None:
        c = is_port(args.ports)
        min_port = c[0]
        max_port = c[1]
    for port in range(min_port, max_port):
        try:
            s = socket.create_connection((host_ip, port))
            opened.append(port)
            sys.stdout.write('.')
            s.close()
        except (ConnectionRefusedError, TimeoutError, socket.timeout):
            pass
    length = len(opened)
    if length > 0:
        sys.stdout.write('\n')
        for num in opened:
            sys.stdout.write(str(num))
            if num != opened[-1]:
                sys.stdout.write(',')
            else:
                if length > 1:
                    sys.stdout.write(' ports are opened')
                else:
                    sys.stdout.write(' port is opened')
    else:
        sys.stdout.write('All doors are closed')
    return 0


if __name__ == '__main__':
    main()

