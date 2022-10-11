import socket

HOST = "127.0.0.1"
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        while True:
            sock.listen();
            conn, addr = sock.accept()
            with conn:
                print(f"accepted socket with addr {addr}")
                conn.send("200 OK\n".encode("utf-8"))
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
            #     print(line)
            #     opcode, arg_1, arg_2 = line.split("\\s")
            #     print(f"opcode {opcode} arg_1 {arg_1} arg_2 {arg_2}")
            #     break
        #         result = 0
        #         did_error = False
        #         if opcode == "+":
        #             result = arg_1 + arg_2
        #         elif opcode == "-":
        #             result = arg_1 - arg_2
        #         elif opcode == "/":
        #             result = arg_1 / arg_2
        #         elif opcode == "*":
        #             result = arg_1 * arg_2
        #         else:
        #             did_error = True
        #         if did_error
        #         conn.send()
        #         print(f"got result {result}")

if __name__=="__main__":
    main()