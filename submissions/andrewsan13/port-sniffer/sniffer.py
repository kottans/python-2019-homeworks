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
                try:
                    data = s.recv(1024)
                except socket.timeout:
                    s = None
                    continue
            if data:
                print('.', end='')
                array_of_ports.append(str(tcp_port))
        else:
            print()
        if array_of_ports:
            print(','.join(array_of_ports) + ' ports are open')
        else:
            print('Host "{}" have no open ports in range {} to {}'.format(host, start_port, end_port))
        return None

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
        host_index = argv.index('--host') + 1  # saving index, where is value for --host

        try:
            host_check = re.fullmatch(r'^(\d{1,3}[.]){3}\d{1,3}$', argv[host_index])  # 123.123.123.123
            host_check2 = re.fullmatch(r'^(\w+[.])+[a-z]+$', argv[host_index])  # google5.com.ua or google.com

            if host_check:

                # each number in IP is less than 256
                less_than_256 = all(int(number) < 256 for number in argv[host_index].split('.'))
                if less_than_256:
                    tcp_ip = argv[host_index]
                else:
                    print('IP or Domain in wrong format')
                    tcp_ip = None
                    
            elif host_check2:
                tcp_ip = argv[host_index]
            else:
                print('IP or Domain in wrong format')
                tcp_ip = None

        except IndexError:
            print('You have no IP address or domain after "--host" in arguments')
            tcp_ip = None

        if '--ports' in argv:
            port_index = argv.index('--ports') + 1  # saving index, where is value for --ports

            try:
                port_check = re.fullmatch(r'^\d+$', argv[port_index])  # only number like a 12345 or other
                port_check2 = re.fullmatch(r'^\d+[-]\d+$', argv[port_index])  # 0-50, number-other_number

                if port_check:
                    ports_range = f'{argv[port_index]}-{argv[port_index]}'  # same (only one number) like a 70-70
                elif port_check2:
                    ports_range = argv[port_index]
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
