import threading
import socket
from types import FunctionType

class WSocket(): 
  
  def __init__(self,name: str, _socket: socket.socket):
    
    self.__onmessage = lambda x: None
    
    
    
  def onmessage(self,callback: FunctionType): 
    self._onmessage = callback
    
