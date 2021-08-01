import socket
import pyautogui

ip = 'SERVER IP'#put the ip of the machine which is running server.py

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
f = s.connect((ip,3902))

def shit():
    while True:
        msg = s.recv(1024)
        f = msg.decode("utf-8")


        if msg.decode("utf-8") == "Request was denied by the host":
            #message when machine running server.py rejects your server start up request
            pyautogui.alert("Request denied from host! If you want to send request again restart the app.")
            break
                

        #sends a request message to the machine running server.py  
        var = pyautogui.confirm('Do you want to request server host to turn on the server?')

        if var == 'OK':
            s.send(bytes("Start_request1","utf-8"))
            
        if var == 'Cancel':
            exit()

shit()