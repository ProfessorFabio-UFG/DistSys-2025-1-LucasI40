import zmq, time, random
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://"+HOST+":"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address

weather_conditions = ["Sunny", "Rainy", "Cloudy", "Stormy"]

while True:
	time.sleep(5)                    # wait every 5 seconds
	
	# Publish current time
	msg = str.encode("TIME " + time.asctime())
	s.send(msg)
	
	# Publish weather update
	weather = random.choice(weather_conditions)
	temp = random.randint(15, 35)
	weather_msg = str.encode(f"WEATHER {weather} {temp}°C")
	s.send(weather_msg)
	

