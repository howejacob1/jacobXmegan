#icky code repitition
import socket

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

def send_str(conn, the_string):
    the_string_with_newline = the_string + "\n"
    conn.sendall(the_string_with_newline.encode("utf-8"))

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind((HOST, PORT))
            while True:
                status_code = 200
                result = -1

                sock.listen()
                
                conn, addr = sock.accept()
                def finish():
                    send_str(conn, f"{status_code} {result}\n")
                    print(f"{line} -> {status_code}")
                try:
                    line = recv_until_newline(conn)
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
                    conn.close()
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
    main()