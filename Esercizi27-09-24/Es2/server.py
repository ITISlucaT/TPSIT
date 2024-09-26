import socket
import threading

server_address = ("127.0.0.1", 6969)
BUFFER_SIZE = 4096

udp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket_server.bind(server_address)

clients = []

def handle_client(client_address, data):
    print(f"Gestione client {client_address}")

    if client_address not in clients:
        clients.append(client_address)
        print(f"Nuovo client connesso: {client_address}")

    for client in clients:
        if client != client_address:  # Non invio il messaggio al mittente
            udp_socket_server.sendto(data, client)
            print(f"Messaggio inoltrato a {client}")

def start_server():
    print(f"Server in ascolto su {server_address}")

    while True:
        data, client_address = udp_socket_server.recvfrom(BUFFER_SIZE)
        print(f"Ricevuto {data.decode('utf-8')} da {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_address, data))
        client_thread.start()

try:
    start_server()
except KeyboardInterrupt:
    print("Chiusura server...")
finally:
    udp_socket_server.close()
