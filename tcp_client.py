import socket

BUFFER_SIZE = 1024
TEST_STRING = 'test'


def start_tcp_client(local_ip, local_port, logger):
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((local_ip, local_port))

    logger(f'Sending {TEST_STRING} to {local_ip}:{local_port} as tcp client')
    socket_client.send(bytes(TEST_STRING.encode('utf-8')))

    msg = socket_client.recv(BUFFER_SIZE).decode('utf-8')
    logger(f'Server answered {msg}')
    socket_client.close()
    logger('Connection closed')
