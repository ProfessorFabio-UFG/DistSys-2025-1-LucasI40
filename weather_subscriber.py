import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "WEATHER")  # subscribe to WEATHER messages

print("Weather Subscriber started. Waiting for weather updates...")

while True:
    weather_data = s.recv()   # receive a message
    print(f"Weather Update: {bytes.decode(weather_data)}") 