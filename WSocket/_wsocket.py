import socket

from . import _wsthread


class WSocket:

    def __init__(self, _socket: socket.socket, name: str = " "):
        self.__onmessage = lambda x: None
        self.__socket = _socket
        self.__name = _socket.getsockname() if name.isspace() else name
        self.__queue = []
        _wsthread.WSThreadRecv(_socket, self.__post_message)
        _wsthread.WSThreadSend(_socket, self.__get_message)

    def getsocket(self) -> socket.socket:
        return self.__socket

    def __post_message(self, msg: str):
        self.__onmessage(msg)

    def __get_message(self):
        if len(self.__queue) != 0:
            return self.__queue.pop(0).encode("utf8")
        else:
            return None

    def onmessage(self, callback) -> None:
        self.__onmessage = callback

    def send(self, data: str):
        self.__queue.append(data)
