import socket

HOST = "127.0.0.1"
PORT = 5000

def do_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen();
        conn, addr = s.accept();
        with conn:
            print(f"connected with {addr}")
            while True:
                # read until a newline
                newline_encountered = False;
                line = ""
                while not newline_encountered:
                    char = conn.recv(1).decode("utf-8")[0];
                    if char == '\n':
                        newline_encountered = True
                    else:
                        line += char
                # we have the line, now simply do an operation on it 
                print(line.split("\\s"))


                
do_server();
