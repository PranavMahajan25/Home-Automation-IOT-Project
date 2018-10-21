import time
import requests
import json
#Access database using firebase url and a config file
firebase_url = 'https://homeautomation-9e67b.firebaseio.com/'
#Setup a loop to send Temperature values at fixed intervals in seconds
import pyrebase
config = {
    'apiKey': "YYY",
    'authDomain': "homeautomation-9e67b.firebaseapp.com",
    'databaseURL': "https://homeautomation-9e67b.firebaseio.com",
    'projectId': "XXXXXXXX",
   'storageBucket': "XXXXXXXX.appspot.com",
   'messagingSenderId': "ZZZ",
}
firebase = pyrebase.initialize_app(config)
timer=0;
while 1:
  try:
    #temperature value set from sensor input          
    temperature_c =str(40)
    #current time and date
    time_hhmmss = time.strftime('%H:%M:%S')
    date_mmddyyyy = time.strftime('%d/%m/%Y')
    day_str = time.strftime("%A")
    day_no = time.strftime("%w")
    #current location name
    
     
    
    #insert record
    data = {'day':day_no,'date':date_mmddyyyy,'time':time_hhmmss,'value':temperature_c}
    if (timer % 10 == 0):
    	result = requests.post(firebase_url + '/' + '/Temperatures.json', data=json.dumps(data))
	print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
	timer=0

    #retrieve data
    db = firebase.database()
    apptemp = db.child("AppValue").get().val()
    print (apptemp)
    appl1 = db.child("Light1").get().val()
    print (appl1)
    
    timer = timer +1
    time.sleep(1)
  except IOError:
    print('Error! Something went wrong.')
time.sleep(1)
