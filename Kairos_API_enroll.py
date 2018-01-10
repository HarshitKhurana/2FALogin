#!/usr/bin/python

# Harshit Khurana
# hkhurana3@gmail.com
# 11.01.18


import requests , json , base64 , sys

def enroll():

	with open(".app_details.txt" , "r")as f:
	    x = f.read()

	app_id = x.split("\n")[0].split(":")[1][1:]
    	app_key = x.split("\n")[1].split(":")[1][1:]

# put your keys in the header
		
	headers = {
	    "Content-Type":"application/json",
	    "app_id": app_id ,
	    "app_key": app_key 
	}


	url = "http://api.kairos.com/enroll"


	# make request
	name = raw_input("Enter the name of the person, whose photos these are: ")
	image_url=''
	payload=''
	gallery_name="Testing"
	print "\n[*] Please enter the path to  "+str(name)+" photos."
	print "[*] Example: /home/ubuntu/Pictures/User1.jpg"
	print "[*] 8 are enough"
	
	error=''
	for i in range(0,8):
	    image_path = raw_input()
	    with open(image_path , "rb")as f:
	        print "Uploading Wait..\n"
	        encoded = base64.b64encode(f.read())
	        payload = {"image": encoded , "subject_id": name , "gallery_name": gallery_name }
	      	try:
	      	    r = requests.post(url, data= json.dumps(payload), headers=headers)
	 	
	        except requests.exceptions.ConnectionError:
 	 		error = 1
 	 		print "No Internet"
 	 		print "Try Again after connecting to Internet"
   	        	sys.exit(0)
	        	break
   	    
	        print "Next Please..."
	if not error:
		print "8 photos of "+name+" uploaded inside '"+gallery_name+" gallery"
#enroll()
