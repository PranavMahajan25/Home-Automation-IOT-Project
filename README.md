# Home-Automation-IOT-Project

**Home Automation / IOT project by Pranav Mahajan in partial fulfillment of Summer Internship 2018 at Mitera Tech.**

Sensory input data from raspberry pi or from arduino (master: raspberry pi and slave: arduino) is sent to firebase using the pyrebasescript.py. One can access the values and change them using the Android App using firebase as realtime database, thus forming a two-way bridge.

1) HomeAutomation.zip conatins Android App source code. Open it in Android Studio. Use the email ID : iotproject997@gmail.com. Can always change the user (top right corner of the window).

2) Access the realtime cloud database through google firebase. Again use the account iotproject997@gmail.com.

3) Run the pyrebasecript.py on the embedded system, Raspberry Pi. In order for it to run forever even after logging out of ssh, use the following comand while executing:`nohup python pyrebassescript.py`<br />
To later stop the process:<br />
When using nohup and you put the task in the background, the background operator (&) will give you the PID at the command prompt.<br />
If your plan is to manually manage the process, you can save that PID and use it later to kill the process if needed, via kill `PID` or `kill -9 PID` (if you need to force kill). <br />
Alternatively, you can find the PID later on by `ps -ef | grep "command name"` and locate the PID from there

for the raspberry pi:<br />
login : pi<br />
passwd: raspberry
