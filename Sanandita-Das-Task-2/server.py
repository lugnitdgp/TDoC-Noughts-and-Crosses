import socket
import sys
import traceback
from threading import Thread

def main():
    start_server()

def start_server():
    host = "127.0.0.1"
    port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")
    try:
        s.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    s.listen(5) #queue up to 5 requests
    print("Socket is now listening")

    while True:
        conn, addr = s.accept()
        ip, port  = str(addr[0]), str(addr[1])
        print("Connected with " + ip + port)
        try:
            Thread(target=clientThread, args=(conn, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()
    s.close()

def clientThread(conn, ip, port, max_buffer_size = 5120):
    is_active = True
    while is_active:
        client_input = receive_input(conn, max_buffer_size)
        if "QUIT" in client_input:
            print("Client is requesting to quit")
            conn.close()
            print("Connection " + ip + " : " + port + " closed.")
            is_active = False
        else:
            print("Processed result: {}".format(client_input))
            conn.sendall("This is the server responding.".encode("utf8"))

def receive_input(conn, max_buffer_size):
    client_input = conn.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))
    decoded_input = client_input.decode("utf8").rstrip()
    result = process_input(decoded_input)
    return result
 
def process_input(input_str):
    print("Processing the input received from client")
    return "Message from client: " + str(input_str).upper()
 
if __name__ == "__main__":
    main()
