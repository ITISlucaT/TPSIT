import socket

server_address = ("127.0.0.1", 6969)
BUFFER_SIZE = 4096

udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(10):
    message = f"ciao sono il client ed è il messaggio numero{i}"
    udp_socket_client.sendto(message.encode("utf-8"), server_address)
    data, server_address = udp_socket_client.recvfrom(BUFFER_SIZE)
    print(f"Ricevuto dal server: {data.decode()}")

udp_socket_client.close()


