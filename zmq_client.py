import zmq #pip install pyzmq
import json
from typing import NamedTuple
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b'acc')
socket.connect("tcp://192.168.85.128:5050")

class Sample(NamedTuple):
    x: float
    y: float
    z: float
    bvp: float
    ibi: float
    tag: float
    timestamp: float


while True:
    #  Wait for next request from client
    # msg = json.loads(socket.recv())
    # sample = Sample(**msg)
    # print(f'Received {sample=}')
    msg = str(socket.recv()).split(' ')[1]
    print(f'Received {msg=}')