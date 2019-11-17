import socket
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='This script displays available ports, for this host or IP',
                                     epilog="Git: github.com/sashalavrus")
    parser.add_argument('--ports', type=str, default="80-450", help="Enter range of ports(example: --ports 10-9999), by defult it's 80-450")
    parser.add_argument('--host', type=str, default="www.google.com", help="Enter the host or IPv4 of host, by default it's www.google.com")
    args = parser.parse_args()
    ports = args.ports.split('-')
    host = args.host
    result = []
    for i in range(int(ports[0]), int(ports[1])):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            s.connect((host, i))
        except socket.error:
            pass
        else:
            result.append(str(i))
            s.close()

    if not result:
        print("Ups, something wrong. Maybe you enter wrong host or IP."
              "If you need help call this script with argument --help")
    else:
        print("Port {0} is open".format(','.join(result)))
