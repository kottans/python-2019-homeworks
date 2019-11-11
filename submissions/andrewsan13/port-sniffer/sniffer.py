def main():
    import socket
    import re
    from sys import argv

    def sniffer(host, start_port, end_port):
        array_of_ports = []

        if not host:
            return None

        for tcp_port in range(start_port, end_port + 1):

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.3)
                try:
                    s.connect((host, tcp_port))
                except OSError:
                    s = None
                    continue
                s.sendall(b'Hello')
                data = s.recv(1024)
            if data:
                print('.', end='')
                array_of_ports.append(str(tcp_port))
        else:
            print()
        if array_of_ports:
            print(','.join(array_of_ports) + ' ports are open')
        else:
            print('Host "{}" have no open ports in range {} to {}'.format(host, start_port, end_port))

    if "--help" in argv:
        print()
        print('TCP sniffer will show you open ports for host')
        print('Use only with argument "--host" in format "--host IP_ADDRESS"(IPv4) or "--host DOMAIN"')
        print('for example:\n--host 172.217.3.110\nor\n--host google.com')
        print()
        print('Also you can limit the range of ports to scan "--ports" in format "--ports <start_port>-<end_port>"')
        print('for example:\n--ports 20-1500')
        print('If you will not using "--ports", for default will using 0-65535')

    if "--host" in argv:
        host_index = argv.index('--host')  # saving index, where is --host

        try:
            host_check = re.fullmatch(r'(\d{1,4}[.]){3}\d{1,4}', argv[host_index + 1])  # 1234.1234.1234.1234
            host_check2 = re.fullmatch(r'(\w+|\d+)+([.]\w+)+', argv[host_index + 1])  # google5.com.ua or google.com

            if host_check or host_check2:
                tcp_ip = argv[host_index + 1]
            else:
                print('IP or Domain in wrong format')
                tcp_ip = None

        except IndexError:
            print('You have no IP address or domain after "--host" in arguments')
            tcp_ip = None

        if '--ports' in argv:
            port_index = argv.index('--ports')  # saving index, where is --port

            try:
                port_check = re.fullmatch(r'\d+', argv[port_index + 1])  # only number like a 12345 or other
                port_check2 = re.fullmatch(r'\d+[-]\d+', argv[port_index + 1])  # 0-50, number-other_number

                if port_check:
                    ports_range = '{0}-{1}'.format(argv[port_index + 1], argv[port_index + 1])  # same (only one number) like a 70-70
                elif port_check2:
                    ports_range = argv[port_index + 1]
                else:
                    print("Wrong format --ports, that's why the program will use default 0-65535")
                    ports_range = '0-65535'

            except IndexError:
                print("You did not specify ports, that's why the program will use default 0-65535")
                ports_range = '0-65535'
        else:
            ports_range = '0-65535'

        min_port = int(ports_range.split('-')[0])
        max_port = int(ports_range.split('-')[1])

        sniffer(host=tcp_ip, start_port=min_port, end_port=max_port)

    else:
        print()
        print('You have no "--host" argument, try again with it')
        return 0


if __name__ == '__main__':
    main()
