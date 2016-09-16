import socket
import time
import logging
import os
import io
import base64

Version = 3 # Include support for POST requests to complete task 2
try:
    os.rename(".\Latest.txt",".\\Logs\\" + time.strftime("%Y%m%d-%H%M%S") + ".txt")
except FileNotFoundError:
    pass
logging.basicConfig(filename=".\Latest.txt",level=logging.DEBUG)

    
print("Starting Bohdan Pike's Python based webserver; Version {}".format(Version))
logging.info("<br>Server version = {}<br>".format(str(Version)))

Port = 80


listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(('', Port))
listen_socket.listen(1)
print('Listening for requests on port {}...\n'.format(Port))
logging.info("<br>Bohdan Pike's Python based webserver is now running on port {}... <br><br>".format(Port))

while True: # Loop forever.
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    
    if request.decode('utf-8').startswith("GET"):
        getrequest = request.decode('utf-8').split("/", 1)[1]
        getrequest = getrequest.split(" ", 1)[0]
        if getrequest != "favicon.ico" and getrequest != "Latest.txt":
            print(request.decode('utf-8'))
            logging.debug("<br>" + request.decode('utf-8') + "<br>")
        try:
            with open ("./HTML/" + getrequest + ".html", "r") as page:
                HTMLPage = page.read()
                logging.info("<br>Sending page: ./HTML/{}.html<br><br>".format(getrequest))
        except FileNotFoundError:
            if getrequest == "":
                with open ("./HTML/main.html", "r") as page:
                    HTMLPage = page.read()
            elif getrequest == "Latest.txt" or getrequest == "InvalidPlates.txt":
                with open (getrequest) as Log:
                    client_connection.sendall(bytes(Log.read(), 'utf-8'))
                    client_connection.close()
                    continue
            elif getrequest == "favicon.ico":
                try:
                    with open("favicon.ico", "rb") as imageFile:
                        f = imageFile.read()
                        client_connection.sendall(bytearray(f))
                        client_connection.close()
                    continue
                except FileNotFoundError:
                    print(" Favicon file couldn\'t be found")
                    logging.error("Favicon file couldn't be found!")
            else:
                print("Page: /{} failed to be found.".format(getrequest))
                logging.error("<br>Page: /{} failed to be found; Sending 404 error.<br><br>".format(getrequest))
                with open ("./HTML/" + "404.html", "r") as page:
                    HTMLPage = page.read()

        client_connection.sendall(bytes(HTMLPage, 'utf-8'))
        client_connection.close()
                    
    elif request.decode('utf-8').startswith("POST"):
        print(request.decode('utf-8'))
        logging.debug("<br>" + request.decode('utf-8') + "<br>")
        postrequest = request.decode('utf-8')
        if "plate=" in postrequest:
            plate = postrequest.split("plate=", 1)[1] # Get assigned variable
            print("Invalid plate infomation detected; {}".format(plate))
            logging.info("<br>&nbsp&nbsp&nbsp&nbspInvalid plate infomation detected; {}".format(plate))
            with open("InvalidPlates.txt", "a") as PlatesLog:
                PlatesLog.write(plate + ", ")
