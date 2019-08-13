from ubidots import ApiClient
import serial 
import time    
import sys

 
try:  
    print "CONNECTED..."  
    arduino = serial.Serial('COM6', 9600, timeout=2.0)
    time.sleep(1)
    arduino.flush()
except:  
    print "CONNECTION FAILURE"


try:  
    print "CONNNECTED API..."  
    api = ApiClient('A1E-1e65f7004a15406fc6a334396d7b5e337e5a')
    temperatura = api.get_variable('5a1e5c80c03f972c4fc70ec2')
except:  
    print "FAILURE CONNECTION API"

contador=0
contador1=0
contador2=0


while True:

	dato=arduino.readline().strip()
	
	if contador == 11:	
		try:
			temp = temperatura.save_value({'value':dato})
		except:
			print "DO NOT SEND" 
		contador=0
		contador1=0
		
	if contador2 == 100:	
		arduino.close()
		arduino = serial.Serial('COM6', 9600, timeout=0.5)
		contador2=0

	
	print(dato)
	contador=contador+ 1
	contador1=contador1+ 1 
	contador2=contador2+ 1 
