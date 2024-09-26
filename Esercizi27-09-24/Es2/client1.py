import socket
import threading

server_address = ("127.0.0.1", 6969)
BUFFER_SIZE = 4096

def receive_messages(udp_socket_client):
    while True:
        try:
            data, server = udp_socket_client.recvfrom(BUFFER_SIZE)
            print(f"\nMittente: {data.decode('utf-8')}")
        except:
            break

udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

threading.Thread(target=receive_messages, args=(udp_socket_client,), daemon=True).start()

try:
    while True:
        message = input("Tu: ")
        udp_socket_client.sendto(message.encode("utf-8"), server_address)

except KeyboardInterrupt:
    print("Chiusura client...")

finally:
    udp_socket_client.close()
