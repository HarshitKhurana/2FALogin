#!/usr/bin/python

# Harshit Khurana
# hkhurana3@gmail.com
# 11.01.18


import requests , json , base64 , sys

with open(".app_details.txt" , "r")as f:
	x = f.read()

app_id = x.split("\n")[0].split(":")[1][1:]
app_key = x.split("\n")[1].split(":")[1][1:]


# put your keys in the header
headers = {

    "app_id": app_id , 
    "app_key": app_key
}

def verify(*arg):

	if len(arg):
		image_path = ''.join(arg)
		#print image_path
	else:
		#print "[*] Example : /home/ubuntu/Pictures/User1.jpg "

		image_path = raw_input("Enter the path of image to check for: ")
	
	with open(image_path ,"rb")as f:
	    encoded = base64.b64encode(f.read())
	    payload =  {"image": encoded , "gallery_name":"Testing" , "subject_id": "salman"}

	url = "http://api.kairos.com/verify"

	# make request
	try:
		r = requests.post(url, data=json.dumps(payload), headers=headers)

		response = {} 
		response = json.loads(r.content)

	except requests.exceptions.ConnectionError:
	#	print "No Internet"

	# If there is no Internet access then the user will simply login, Uncomment this, if you do not want this i.e if no internet access then the user will not be able to login.
	#	os.system("killall -u `whoami`")
		sys.exit(0)

	#print response
	
	if 'Errors' in str(response):
		#print "error"
		return "error"
	else:
		#print response['images']
		list_response = response['images']
		confidence = 100 *  list_response[0]['transaction']['confidence']
		#print "Confidence is: "+str(confidence)
		return int(confidence)

#verify('Images_OpenCV/Image.jpg')
