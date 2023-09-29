import zmq #pip install pyzmq
import json
from typing import NamedTuple
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b'')
socket.connect("tcp://192.168.0.208:5050")

class Sample(NamedTuple):
    x: float
    y: float
    z: float
    bvp: float
    ibi: float
    tag: float
    timestamp: float



wanted_keys = ['bvp', 'ibi', 'x', 'y', 'z', 'tag', 'timestamp']
while True:
    #  Wait for next request from client
    msg = json.loads(socket.recv())
    msg = {k:(-1 if msg[k]=='' else float(msg[k])) for k in wanted_keys}
    sample = Sample(**msg)
    print(f'Received {sample=}')