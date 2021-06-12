import socket
import cv2
import pickle
import struct
server_side = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print ("our host ip is :",host_ip)
port = 1845
server_address = ('25.189.202.208',port)
server_side.bind((host_ip,port))
print("socket bind successfully")
server_side.listen(5)
print("LISTENING AT THIS IP AND PORT:",server_address)
print("socket task done")
while True:
    client_side,addr = server_side.accept()
    print('Got THe Connection From The :',addr)
    if client_side:
        vid = cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_side.sendall(message)
            
            cv2.imshow('Server side video',frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                 client_side.close()
        

