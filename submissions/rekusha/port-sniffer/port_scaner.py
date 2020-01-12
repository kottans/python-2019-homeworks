import socket
import argparse
import sys


def port_scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        s.connect((host, port))
        return True
    except Exception:
        return False
    finally:
        s.settimeout(None)


def main(host, ports='0-65535'):
    start_port, end_port = ports.split('-')
    opened_port = []
    for x in range(int(start_port), int(end_port)+1):
        if port_scan(host, x):
            sys.stdout.write('.')
            opened_port.append(x)
    sys.stdout.write(f"\n{str(opened_port).strip('[').strip(']')} ports are opened") if len(opened_port) > 0 \
        else sys.stdout.write('No open ports')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Port scanner, for use run programm with param --host <name or ip> and '
                                                 '--ports <range> (ports by default have value 0-65535)')
    parser.add_argument('--host', help='enter host or IP', required=True)
    parser.add_argument('--ports', help='enter of start and end scan ports like 0-65535')
    args = parser.parse_args()
    main(args.host, args.ports)
