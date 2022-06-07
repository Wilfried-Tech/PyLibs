# import socket

# from wsocket._wsocket import WSocket

# s = input("serveur ou client")
# address = 'localhost'
# port = 5000

# conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# def scmsg(m):
#     print("onmessage sclient", m.decode("utf8"))


# def cmsg(m):
#     print("onmessage client", m.decode("utf8"))


# if int(s) == 1:
#     conn.bind((address, port))
#     conn.listen(1)
#     client, address = conn.accept()
#     wclient = WSocket(client)
#     wclient.send("it work")
#     wclient.onmessage(scmsg)
# else:
#     conn.connect((address, port))
#     wclient = WSocket(conn)
#     wclient.onmessage(scmsg)
#     wclient.send("it work")

from pystrictdef.strict import checkType


@checkType(int, int)
def test(a, b):
    pass

test("",5)