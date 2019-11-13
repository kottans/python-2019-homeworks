import socket, argparse, sys

def parserfun():
    parser = argparse.ArgumentParser(description="TCP scanner search ports")
    parser.add_argument("--host", help=" type host, example: www.google.com",type=str, metavar="host", required=True)
    parser.add_argument("--ports", type=range, metavar="start_port - end_port", nargs=2, default=[0, 65535], help="3-600")
    return parser

args = parserfun().parse_args()

def scanner(host, start_port, end_port):
    buffer = []
    for port in range(start_port, end_port + 1):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(0.3)
        result = connection.connect_ex((host, port))

        if result == 0:
            op.append(port)
            print(".", end="")
            sys.stdout.flush()
        connection.close()
    print("\n")
    return buffer

try:
 ports = scanner(args.host, args.ports[0], args.ports[1])
except (KeyboardInterrupt, socket.gaierror, socket.error) as error:
  print(error)
  sys.exit()

if ports:
  print("Check: " + ", ".join(map(str, ports)))
else:
  print("No open ports")