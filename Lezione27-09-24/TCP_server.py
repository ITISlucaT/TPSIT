import socket

server_address = ("192.168.1.136", 6971)
BUFFER_SIZE = 4096 

commands_dict = ["forward","backward","right","left"]

menu_message = """
USAGE: #command_name #value(0-100)
    1 - forward
    2 - backward
    3 - right
    4 - left
"""

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(server_address)

tcp_server_socket.listen(1)
print(f"Server in ascolto su {server_address}")

conn, client_address = tcp_server_socket.accept()
print(f"Connesso al client {client_address}")

conn.send(menu_message.encode("utf-8"))

try:
    while True:
       
        data = conn.recv(BUFFER_SIZE).decode("utf-8")
        command, value = data.split(" ")
        print(f"Command: {command} value {value}")
        
        if not data:
            break  

        print(f"Ricevuto dal client: {data}")
        
        # Esegui logica sui comandi
except KeyboardInterrupt:
    print("Chiusura server")
finally:
    tcp_server_socket.close()
