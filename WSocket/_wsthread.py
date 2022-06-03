from socket import socket
from threading import Thread


class WSThreadRecv(Thread):

    def __init__(self, connection: socket, recv_callback, stop_callback=None) -> None:
        Thread.__init__(self)
        self.__connection = connection
        self.__callback = recv_callback
        self.__stop = stop_callback

    def run(self) -> None:
        data = b''
        while True:
            octets = self.__connection.recv(1024)
            if not octets:
                print("fin reception")
                self.__connection.close()
                if self.__stop is not None:
                    self.__stop()
                break
            data += octets
        print("calling recv callback")
        self.__callback(data)


class WSThreadSend(Thread):

    def __init__(self, connection: socket, send_callback, stop_callback=None) -> None:
        Thread.__init__(self)
        self.__connection = connection
        self.__callback = send_callback
        self.__stop = stop_callback

    def run(self) -> None:
        while True:
            data: str = self.__callback()
            if data is not None:
                print("sending ...")
                self.__connection.send(data)
