import socket

BUFFER_SIZE = 1024


def start_udp_server(local_ip, local_port, logger):
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind((local_ip, local_port))

    logger(f"UDP server up at {local_ip}:{local_port} and listening")

    while True:
        bytes_address_pair = udp_server_socket.recvfrom(BUFFER_SIZE)

        message = bytes_address_pair[0].decode('utf-8')
        address = bytes_address_pair[1]

        msg_from_server = f"Echo {message} from {address}"
        logger(msg_from_server)

        bytes_to_send = str.encode(msg_from_server)

        udp_server_socket.sendto(bytes_to_send, address)
        logger('Connection with client closed')
