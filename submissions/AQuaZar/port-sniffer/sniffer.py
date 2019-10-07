import sys
import argparse
import socket


def range_type(astr, minimal=0, maximal=65535):
    value = int(astr)
    if minimal <= value <= maximal:
        return value
    else:
        raise argparse.ArgumentTypeError(
            "value not in range {min}-{max}".format(minimal, maximal)
        )


parser = argparse.ArgumentParser(
    description="""Output a list of opened TCP ports on specified host. 
    By default all ports in range (0..65535) will be checked"""
)

parser.add_argument(
    "--host",
    metavar="Host",
    type=str,
    help="IPv4 address or domain name, which ports to check e.g. www.google.com, 192.168.0.1, e.t.c ",
    required=True,
)
parser.add_argument(
    "--ports",
    metavar=("First", "Last"),
    type=range_type,
    nargs=2,
    default=[0, 65535],
    help="To check specific range of ports, define first and last port from range, e.g. --ports 69 420",
)

args = parser.parse_args()


def port_scan(host, first, last):
    print("Searching")
    open_ports = []
    for port in range(first, last + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((host, port))

        if result == 0:
            open_ports.append(port)
            print(".", end="")
            sys.stdout.flush()
        sock.close()
    print("\n")
    return open_ports


if __name__ == "__main__":
    ports = []
    try:
        ports = port_scan(args.host, args.ports[0], args.ports[1])
    except KeyboardInterrupt:
        print("Interrupted by user")
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    if len(ports) == 0:
        print("Not found any opened ports on desired host")
    elif len(ports) == 1:
        print("Port {0} is opened".format(ports[0]))
    else:
        print(("Ports " + ", ".join(map(str, ports)) + " are opened."))
