import output
import requests
import json

class InitialState(output.Output):
	print "InitialState: Initializing Class"
	requiredData = ["BucketKey","AccessKey"]
	optionalData = []
	def __init__(self,data):
		self.BucketKey=data["BucketKey"]
		self.AccessKey=data["AccessKey"]
		print "InitialState: Read the Keys from outputs.cfg"
	def outputData(self,dataPoints):
		arr = []
		print "InitialState: Populating Array"
		for i in dataPoints:
			arr.append({"key":i["name"],"value":i["value"]})
		print "InitialState: Converting Array to JSON"
		a = json.dumps(arr)
		print a
		try:
			print "InitialState: Executing requests.post()"
			z = requests.post("https://groker.initialstate.com/api/events",headers={'Content-Type': 'application/json','X-IS-AccessKey':self.AccessKey,'X-IS-BucketKey':self.BucketKey,'Accept-Version': '0.0.4'},data=a)
			if z.text!="": 
				print "InitialState: POST Error: " + z.text
				return False
		except Exception:
			return False
		return True
