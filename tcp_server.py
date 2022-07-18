import socket

BUFFER_SIZE = 1024


def start_tcp_server(local_ip, local_port, logger):
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind((local_ip, local_port))

    logger(f"TCP server up at {local_ip}:{local_port} and listening")
    tcp_server_socket.listen(1)
    while True:
        socket_client, (address, port) = tcp_server_socket.accept()
        message = socket_client.recv(BUFFER_SIZE).decode('utf-8')

        msg_from_server = f"Echo {message} from {address}:{port}"
        logger(msg_from_server)

        bytes_to_send = str.encode(msg_from_server)

        socket_client.send(bytes_to_send)
        socket_client.close()
        logger('Connection with client closed')
