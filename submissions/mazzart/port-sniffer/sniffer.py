import argparse
import socket
import sys


def argument_parser():
    """Initialize argument parser"""

    script_description = "Sniffer is tool which allows user to easily " \
                         "search for opened TCP ports on particular host"

    parser = argparse.ArgumentParser(description=script_description)
    parser.add_argument('--host', type=str, nargs='?', required=True,
                        help='enter domain name or IP address to search')
    parser.add_argument('--ports', type=str, nargs='?', default='0-65535',
                        help='limit the range of ports to scan, '
                             'use the format: <start_port>-<end_port>')

    return parser


def ports_scanner(host: str, ports: str) -> list:
    """Scans and saves open TCP ports"""

    buffer = []
    start, end = ports.split('-')
    start, end = int(start), int(end)

    try:
        for port in range(start, end+1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.3)
                conn = sock.connect_ex((host, port))
                if conn == 0:
                    print('.', end='')
                    buffer.append(port)
                else:
                    continue

    except KeyboardInterrupt:
        print("You printed Ctrl+C")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
    except socket.error as error:
        print(error)
        sys.exit()

    return buffer


def show_ports(ports_list: list):
    """Prints ports info"""

    if ports_list:
        print()
        for port in ports_list:
            print(port, end=',')
        print(' ports are opened')
    else:
        print('There are no open ports')


def main():
    """Script entry point"""

    args = argument_parser().parse_args()
    argv = vars(args)
    host, ports = argv['host'], argv['ports']
    open_ports = ports_scanner(host, ports)
    show_ports(open_ports)


if __name__ == "__main__":
    main()
