import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages

print("Time Subscriber started. Waiting for time updates...")

while True:
	time_data = s.recv()   # receive a message
	print(f"Time Update: {bytes.decode(time_data)}")
