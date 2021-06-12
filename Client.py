# Client (c)

import socket
import cv2
import struct
import pickle 
client_side = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip ='192.168.43.231'
port = 1845
client_side.connect((host_ip,port))
data = b""
payload_size = struct.calcsize("Q")
print("socket accept")
while True:
    while len(data)<payload_size:
        packet = client_side.recv(2160)
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]
    
    while len(data) < msg_size:
        data+= client_side.recv(2160)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("Client video live", frame)
    key = cv2.waitKey(1) & 0xFF
    if key ==ord('q'):
        break

client_side.close()
