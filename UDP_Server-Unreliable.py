#icky code repitition
import socket
import random
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

def send_str(sock, the_string, addr):
    sock.sendto(the_string.encode("utf-8"), addr)

buffer_size = 1024*1024

def main(percent_chance, seed):
    random.seed(seed)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind((HOST, PORT))
            while True:
                status_code = 200
                result = -1
                bytes, addr = sock.recvfrom(buffer_size)
                line = bytes.decode("utf-8")
                line = line.strip()
                if random.random() < percent_chance:
                    print(f"{line} -> dropped")
                else:
                    def finish():
                        send_str(sock, f"{status_code} {result}\n", addr)
                        print(f"{line} -> {status_code} {result}")
                    
                    opcode, arg_1_str, arg_2_str = line.split()
                    if not is_opcode_valid(opcode):
                        status_code = 620
                    else:
                        try:
                            arg_1 = int(arg_1_str)
                            arg_2 = int(arg_2_str)
                        except ValueError:
                            status_code = 630
                        else:
                            if 0 in [arg_1, arg_2]:
                                status_code = 630
                            else:
                                # now calculate what really happened
                                if opcode == "+":
                                    result = arg_1 + arg_2
                                elif opcode == "-":
                                    result = arg_1 - arg_2
                                elif opcode == "/":
                                    result = arg_1 / arg_2
                                elif opcode == "*":
                                    result = arg_1 * arg_2
                                else:
                                    print("in trouble now")
                    finish()
        finally:
            sock.close()

                # while True:
                #     # read until a newline
                #     newline_encountered = False;
                #     line = ""
                #     while not newline_encountered:
                #         char = conn.recv(1).decode("utf-8")[0];
                #         if char == '\n':
                #             newline_encountered = True
                #         else:
                #             line += char
                #     # we have the line, now simply do an operation on it 

if __name__=="__main__":
    main(float(sys.argv[1]), sys.argv[2])