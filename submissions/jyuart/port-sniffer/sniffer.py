import socket
import click

opened_ports = []

def sniff(ip, ports):
	start_port = int((ports.split("-"))[0])
	end_port = int((ports.split("-"))[1])
	for current_port in range(start_port, end_port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.3)
		result = s.connect_ex((ip, current_port))
		if result == 0:
			print(".", end="")
			opened_ports.append(str(current_port))
	if not (opened_ports):
		print("There are no opened ports in this range:", ports)
	else:
		print("\n", ((", ").join(opened_ports)), " ports are opened", sep="")


@click.command()
@click.option("--host", metavar="<domain name or ip>", help="it can be either domain name or IP address")
@click.option("--ports", metavar="<range of numbers>", default="0-65535", help="it should be two integers divided by hyphen")
def main(host, ports):
	""" Sniffer is CLI tool which allows user to easily search for opened TCP ports on particular host (using IP adderess or domain)"""
	sniff(host, ports)


try:
	if __name__ == "__main__":
		main()

except socket.gaierror:
	print("This host is not valid. \nIt can be either domain name, like google.com or IP address like 172.217.3.110")

except ValueError:
	print("Format of either host or ports is incorrect.\nHost should be domain name like google.com or IP like 172.217.3.110.\nPorts should be a range of numbers like 0-80")

except TypeError:
	print("Parameter host is required. \nIt can be either domain name, like google.com or IP address like 172.217.3.110")

except IndexError:
	print("You've entered one number.\nThere should be a range of ports divided by hyphen.")