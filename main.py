import socket

target_addr = input("Please type in the target IP address: ")
port_range = input("Please type in the port range, ex. 0 - 200: ")

lowpoint = int(port_range.split("-")[0])
highpoint = int(port_range.split("-")[1])

for port in range(lowpoint, highpoint):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target_addr, port))
    if(result == 0):
        print("*** Port",port," - is open.***")
    else:
        print("*** Port",port," - is closed.***")    
s.close()