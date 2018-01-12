* Harshit Khurana
* hkhurana3@gmail.com
* 11.01.18


2FALogin : It is a program which provides 2Factor Authentication using Face recognition with the help of Kairos API.


* As soon as you cross the Password based authentication on your system the 2FALogin will automatically begin and if the user(Image of user) does not matches, It will log you out and the login process will have to be started over from the top.

* InCase the system is booted without internet access then 2FALogin will not run and user will directly be able to login.
  To counter this , Uncomment the line `"os.system("killall -u `whoami`")"` in 'Kairos_API_verify.py", Then if the internet is not available at booting time the user will not be allowed to login.

* Incase using the 2FALogin wth Raspberry Pi and external USB Camera, ensure you skip around 5 frames( may varry) before using the actual frame/image for comparison.
  
  Could do this simply by replacing "ret,frame = cap.read() " in 'CameraCapture.py' with:
  	
  	`for i in (0,5):
  		ret,frame = cap.read() `

Tried and Tested using python2.7 and Ubuntu 16.04.3 LTS/Raspberry Pi.

You need to have a kairos developer account in order to use the script.

Make an account at https://developer.kairos.com/signup and get the "app_id" and "app_key".

INSTALLATION :

* To install all the necessary dependencies run:

	` pip install -r requirements.txt`	
 
* To install 2FALogin in your system simply run:

	` python Install.py`

EXECUTION :

* To execute 2FALogin simply run:

	 ` python Run.py `
