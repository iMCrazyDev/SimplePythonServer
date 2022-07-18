import argparse
import ipaddress
import logging
import sys

import tcp_client
import udp_client
import udp_server
import tcp_server

parser = argparse.ArgumentParser(description='Starting a TCP/UDP Server which listen certain IP'
                                             'or a Client \n which send simple request')
parser.add_argument('-s', help='stars as server (default as client)', action="store_true")
parser.add_argument('-t', help='working as tcp', action="store_true")
parser.add_argument('-u', help='working as udp', action="store_true")
parser.add_argument('-f', help='specify output')
parser.add_argument('ip', help='specify ip addr and port ex. 0.0.0.0')
parser.add_argument('port', help='specify port', type=int)

args = parser.parse_args()


def validate_ip(addr):
    try:
        ipaddress.ip_address(addr)
        return True
    except ValueError:
        return False


if args.u and args.t:
    print('error: you should select only one type of connection tcp or udp')
    sys.exit()
elif args.u == args.t:
    args.t = True

if not validate_ip(args.ip) or args.port < 0 or args.port > 65535:
    print('invalid ip and/or port argument')
    sys.exit()

if args.f:
    logging.basicConfig(filename=args.f, format='[%(asctime)s] %(message)s', datefmt='%I:%M:%S',
                        encoding='utf-8', level=logging.INFO)
else:
    logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%I:%M:%S', level=logging.INFO)

logging.info('Valid arguments, starting...')

if args.s:
    if args.t:
        server = tcp_server.start_tcp_server
    else:
        server = udp_server.start_udp_server

    server(args.ip, args.port, logging.info)
else:
    if args.t:
        client = tcp_client.start_tcp_client
    else:
        client = udp_client.start_udp_client

    client(args.ip, args.port, logging.info)
