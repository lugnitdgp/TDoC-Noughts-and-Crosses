import socket
import sys
def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 9999
    try:
        soc.connect((host, port))
    except:
        print("Connection Error")
        sys.exit()
    while True:
        message = input("Enter message, enter 'quit' to exit: ")
        if message == 'quit':
            break
        soc.sendall(message.encode("utf8"))
        print("Received message :", soc.recv(5120).decode("utf8"))
    soc.send(b'quit')

if __name__ == "__main__":
    main()
