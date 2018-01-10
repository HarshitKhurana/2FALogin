#!/usr/bin/python

# Harshit Khurana
# hkhurana3@gmail.com
# 11.01.18


import Kairos_API_enroll as Kairos_API_enroll
import os


os.system('chmod +x $PWD/Run.py && echo "cd $PWD && python Run.py; cd" >> $HOME/.profile')

print "Please provide the app_id and app_key for your kairos developer account."

app_id = str(raw_input("Enter App_id: "))
app_key = str(raw_input("Enter App_key: "))

with open(".app_details.txt" , "w")as f:
	f.write("App_id: "+str(app_id)+"\n")
	f.write("App_key: "+str(app_key))
	f.write("\n")
Kairos_API_enroll.enroll()


