import socket
import os
import pyautogui

ip = '0.0.0.0'#no need to change this ip, "0.0.0.0" will be ur pc's ip address so just change the ip in the client.py to the ip of machine running server.py

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,3902))
s.listen(100)

def shit():
    while True:
        clientsocket, address = s.accept()

        pyautogui.alert(f"Connecting from {address} has been established")

        clientsocket.send(bytes("Welcome to the server!", "utf-8"))

        msg = clientsocket.recv(1024)
        print(msg.decode("utf-8"))


        if msg.decode("utf-8") == 'Start_request1':
            var = pyautogui.confirm('Do you wish to start server?')
            if var == ("OK"):
                os.startfile('Server.lnk')#change 'Server.lnk' to your server.jar or run.bat (make sure tht this file is in that folder/directory)
                

            else:
                var = clientsocket.send(bytes("Request was denied by the host","utf-8"))
                print(var)


shit()
