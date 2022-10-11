#icky code repitition
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

def is_opcode_valid(opcode):
    valid_opcodes = ["+", "-", "/", "*"]
    return opcode in valid_opcodes

def send_str(conn, the_string, addr_and_port):
    conn.sendto(the_string.encode("utf-8"), addr_and_port)

BUFFER_SIZE = 1024*1024
    
opcode_descs = {620: "Invalid OC",
                630: "Invalid operands"}

def main(filename):
    with open(filename) as file_handle:
        for example_line in file_handle.read().split("\n"):
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as conn:
                send_str(conn, example_line + "\n", (HOST, PORT))
                line = conn.recvfrom(BUFFER_SIZE)
                status_code, result = line.split()
                try:
                    status_code = int(status_code)
                    if status_code == 200:
                        print(f"Result is {result}")
                    else:
                        print(f"Error {status_code}: {opcode_descs[status_code]}")
                except ValueError:
                    print("bad status_code")
                finally:
                    conn.close()
        file_handle.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main("example_data.txt")