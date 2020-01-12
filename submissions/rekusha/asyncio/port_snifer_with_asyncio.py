import asyncio
import argparse
import sys


async def check_port(ip, port, loop):
    conn = asyncio.open_connection(ip, port, loop=loop)
    try:
        reader, writer = await asyncio.wait_for(conn, timeout=0.3)
        print('.', end='')
        opened_port.append(port)
    except:
        pass


async def check_port_sem(sem, ip, port, loop):
    async with sem:
        return await check_port(ip, port, loop)


async def run(dest, ports, loop):
    sem = asyncio.Semaphore(400)
    tasks = [asyncio.ensure_future(check_port_sem(sem, dest, p, loop)) for p in ports]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Port scanner, for use run programm with param --host <name or ip> and '
                                                 '--ports <range> (ports by default have value 0-65535)')
    parser.add_argument('--host', help='enter host or IP', required=True)
    parser.add_argument('--ports', help='enter of start and end scan ports like 0-65535')

    args = parser.parse_args()
    start_port, end_port = args.ports.split('-')
    dest = args.host
    ports = list(range(int(start_port), int(end_port)+1))
    opened_port = []

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(dest, ports, loop))
    loop.run_until_complete(future)

    sys.stdout.write(f"\n{str(opened_port).strip('[').strip(']')} ports are opened") if len(opened_port) > 0 \
        else sys.stdout.write('No open ports')
