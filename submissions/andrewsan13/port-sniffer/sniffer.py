import socket
import re
from sys import argv


def empty():
    return 0


def sniffer(host, start_port, end_port):
    array_of_ports = []

    if not host:
        return 0

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
        #if len(array_of_ports) == 1:
        #    print('{} port are open'.format(array_of_ports[0]))
        #else:
        #    for i in array_of_ports:
        #        print(str(i) + ',', end='')
        #    print(' ports are open')
    else:
        print('Host "{}" have no open ports in range {} to {}'.format(host, start_port, end_port))


if "--help" in argv:
    print('TCP sniffer will show you open ports for host')
    print('Use only with argument "--host" in format "--host IP_ADDRESS"(IPv4) or "--host DOMAIN"')
    print('for example:\n--host 172.217.3.110\nor\n--host google.com')
    print()
    print('Also you can limit the range of ports to scan "--ports" in format "--ports <start_port>-<end_port>"')
    print('for example:\n--ports 20-1500')
    print('If you will not using "--ports", for default will using 0-65535')

if "--host" in argv:
    HOST = argv.index('--host')  # saving index, where is --host

    try:
        host_check = re.fullmatch(r'(\d{1,4}[.]){3}\d{1,4}', argv[HOST + 1])  # 1234.1234.1234.1234
        host_check2 = re.fullmatch(r'(\w+|\d+)+([.]\w+)+', argv[HOST + 1])  # google5.com.ua or google.com

        if host_check or host_check2:
            TCP_IP = argv[HOST + 1]
        else:
            print('IP or Domain in wrong format')
            TCP_IP = None

    except IndexError:
        print('You have no IP address or domain after "--host" in arguments')
        TCP_IP = None

    if '--ports' in argv:
        PORT = argv.index('--ports')  # saving index, where is --port

        try:
            port_check = re.fullmatch(r'\d+', argv[PORT + 1])  # only number like a 12345 or other
            port_check2 = re.fullmatch(r'\d+[-]\d+', argv[PORT + 1])  # 0-50, number-other_number

            if port_check:
                PORTS = '{0}-{1}'.format(argv[PORT + 1], argv[PORT + 1])  # same (only one number) like a 70-70
            elif port_check2:
                PORTS = argv[PORT + 1]
            else:
                print("Wrong format --ports, that's why the program will use default 0-65535")
                PORTS = '0-65535'

        except IndexError:
            print("You did not specify ports, that's why the program will use default 0-65535")
            PORTS = '0-65535'
    else:
        PORTS = '0-65535'

    TCP_PORT_MIN = int(PORTS.split('-')[0])
    TCP_PORT_MAX = int(PORTS.split('-')[1])

    sniffer(host=TCP_IP, start_port=TCP_PORT_MIN, end_port=TCP_PORT_MAX)

else:
    print()
    print('You have no "--host" argument, try again with it')
    empty()