import socket

BUFFER_SIZE = 1024
TEST_STRING = 'test'


def start_udp_client(local_ip, local_port, logger):
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    logger(f'Sending {TEST_STRING} to {local_ip}:{local_port} as udp client')
    socket_client.sendto(bytes(TEST_STRING.encode('utf-8')), (local_ip, local_port))
    msg, addr = socket_client.recvfrom(BUFFER_SIZE)
    logger(f'Server {addr} answered {msg.decode("utf-8")}')
    socket_client.close()
    logger('Connection closed')
