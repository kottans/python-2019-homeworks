import click
import socket


@click.command()
@click.option('--host', default=False,
              help='Host. Can be IP address or domain name. Mandatory argument')
@click.option('--ports', default='1-65535',
              help='Ports range in format like 1-100. Default value is 1-65535')
def main(host, ports):
    """Finds available ports on specific host. Timeout set to 300ms"""

    # if no host specified close the program
    if not host:
        print('Please enter host address')
        exit(-1)

    # convert ports argument value to range
    port_left_lim = int(ports.split('-')[0])
    port_right_lim = int(ports.split('-')[1])
    ports = range(port_left_lim, port_right_lim + 1)

    available_ports = get_ports(host, ports)
    if available_ports:
        print('\n', ','.join(available_ports), ' ports are opened')
    else:
        print('No port available')


def get_ports(host, ports):
    # list to save available ports
    buffer = []

    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)
            try:
                con = s.connect((host, port))
            except socket.timeout:
                continue
            else:
                # if connection was successful save port
                buffer.append(str(port))
                print('.', end='', flush=True)
    return buffer


if __name__ == '__main__':
    main()
