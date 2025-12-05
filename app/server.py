import socket

DATA_STORE = {}

def server():
    # AF_INET means use ipv4
    # SCOK_STREAM to use TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind("127.0.0.1", 6379)
    # 5 max connections at a time
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        print(f"New connection from {addr}")
        

        while True:
            request = client_socket.recv(1024).decode("utf-8")

            if not request:
                break

            response = "ERROR\n"

            parts = request.split(" ")
            request_type = parts[0]

            if request_type == "SET" and len(parts) > 2:
                request_key = parts[1]
                request_data = " ".join(parts[2:])
                DATA_STORE[request_key] = request_data
                response = "OK\n"

            elif request_type == "GET" and len(parts) > 1:
                request_key = parts[1]
                response = DATA_STORE.get(request_key, "nil\n") + "\n"

            elif request_type == "EXIT":
                client_socket.send("BYE\n".encode())
                break

            client_socket.send(response.encode)
            
        client_socket.close()


if __name__ == "__main__":
    print("Server Started...")
    server()