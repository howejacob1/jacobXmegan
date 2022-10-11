from re import S
import socket
import sys

HOST = "127.0.0.1"
PORT = 5000

def recv_until_newline(something_that_can_recv):
    conn = something_that_can_recv
    newline_encountered = False;
    line = ""
    while not newline_encountered:
        char = conn.recv(1).decode("utf-8")[0];
        if char == '\n':
            newline_encountered = True
        else:
            line += char
    return line

def main(filename):
    with open("example_data.txt") as file_handle:
        for line in file_handle.readlines():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
                conn.connect((HOST, PORT))
                print(f"connected to {HOST}:{PORT}")
                conn.sendall(line.encode("utf-8"))
                print(f"got {recv_until_newline(conn)}")

if __name__ == "__main__":
    main(sys.argv[1])