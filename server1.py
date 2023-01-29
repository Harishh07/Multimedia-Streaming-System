# This is server code to send audio frames over TCP
import cv2
import socket 
import threading, wave, pyaudio,pickle,struct  

host_name = socket.gethostname()
host_ip = '192.168.43.91'#  socket.gethostbyname(host_name)
print('Host IP:',host_ip)
port = 9611

def audio_stream():
    server_socket = socket.socket()
    server_socket.bind((host_ip, (port-1)))
    print('Socket Binding completed')
    server_socket.listen(5) #server can listen upto 5 clients
    CHUNK = 1024
    wf = wave.open("temp1.wav", 'rb')
    
    p = pyaudio.PyAudio()
    print('Server listening at:',(host_ip, (port-1)))
   
    
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    input=True,
                    frames_per_buffer=CHUNK)

             

    client_socket,addr = server_socket.accept()
 
    data = None
    while True:
        if client_socket:
            while True:
              
                data = wf.readframes(CHUNK)
                a = pickle.dumps(data)
                message = struct.pack("Q",len(a))+a  #q is long long int
                client_socket.sendall(message)
                

t1 = threading.Thread(target=audio_stream, args=())
t1.start()
