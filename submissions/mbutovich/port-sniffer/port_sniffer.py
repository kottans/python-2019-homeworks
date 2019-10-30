import argparse
import socket
import sys


def main():
    func_description = '''Sniffer is a tool which allows user to easily search 
                        for opened TCP ports on particular host (using IP address 
                        or domain). If dial is successful program will print dot . to stdout.
                        IMPORTANT: Each dial attempt has 300ms timeout.
                        After scan is finished program will print the list of opened
                        ports to stdout and exit with status code 0'''
    parser = argparse.ArgumentParser(description=func_description)
    parser.add_argument('--ports', type=str, default='0-65536',
                        help=('range of ports to scan, format <start_port>-<end_port> '
                              '(default min-max range: 0-65535)'))
    parser.add_argument('--host', type=str, required=True,
                        help=('required argument, can be either domain name, like google.com'
                              ' or IP address like 172.217.3.110'))
    args = parser.parse_args()

    def check_ports(ports):
        if (ports.count('-') == 1
                and all(i.isdigit() for i in args.ports.split('-'))
                and all(int(i) in range(0, 65536) for i in args.ports.split('-'))):
            return True
        return False

    def sniff_ports(host, ports):
        if not check_ports(ports):
            raise ValueError('Ports should be passed in format <start_port>-<end_port>')
        open_ports = []

        for i in range(*(int(i) for i in args.ports.split('-'))):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.3)
                    if sock.connect_ex((host, i)) == 0:
                        print('.')
                        open_ports.append(i)

            except socket.timeout:
                continue

            except KeyboardInterrupt:
                print('Process was interrupted by user.')
                sys.exit(-1)

            except socket.gaierror:
                print('Hostname could not be resolved.')
                sys.exit(-1)

            except socket.error as e:
                print(e)
                sys.exit(-1)

        message = f'{open_ports} ports are open' if len(open_ports) != 0 else '0 open ports found'
        print(f'{message} in range {args.ports} at {args.host}.')
        sys.exit(0)

    sniff_ports(args.host, args.ports)


if __name__ == '__main__':
    main()
