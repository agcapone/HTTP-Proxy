#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      tcpserver.py
#
#      Copyright 2014 Recursos Python - www.recursospython.com
#
#
from socket import socket, error
from threading import Thread
import post_echo
import get_jwt


class Client(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """
    
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)
        
        self.conn = conn
        self.addr = addr
    
    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                
                input_data = self.conn.recv(1024)
                print(input_data)
                print("The user entered is: " + input_data.decode("utf-8","ignore"))
                transform = post_echo.post_token(input_data)

            except error:
                print("[%s] Read Error." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if input_data:
                    self.conn.send(transform)
                    

def main():
    s = socket()
    
    # Escuchar peticiones en el puerto 9097.
    host = "127.0.0.1"
    port= 9097
    s.bind((host, port))
    print("Proxy server is running on {}:{}".format(host, port))
    s.listen(0)
    
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("New connection from %s:%d " % addr)
if __name__ == "__main__":
    main()