import json
import time
import urllib2

i = 1
while True:
	
	rnd = urllib2.urlopen("https://www.random.org/integers/?num=1&min=1&max=5&col=1&base=10&format=plain&rnd=new").read().strip()
	print int(rnd)

	data = {"amount":int(rnd), "orderId" : i}

	req = urllib2.Request("http://localhost:8081/randomOrder")
	req.add_header("Content-Type","application/json")
	urllib2.urlopen(req, json.dumps(data)).read()

	i = i+1
	time.sleep(10.0)