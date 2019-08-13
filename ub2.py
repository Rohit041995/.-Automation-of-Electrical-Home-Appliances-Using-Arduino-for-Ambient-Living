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
    #api = ApiClient('A1E-1e65f7004a15406fc6a334396d7b5e337e5a')
    ldr_id = api.get_variable('5a1e5c80c03f972c4fc70ec2')
    hum_id = api.get_variable('5a1e7cadc03f9754e4b67571')
    temp_id = api.get_variable('5a1e7c20c03f9754c52b0937')
except:  
    print "FAILURE CONNECTION API"

contador=0
contador1=0
contador2=0


while True:

	dato=arduino.readline().strip()
	l = dato.split(',')
        ldr = l[0]
        hum = l[1]
        temp = l[2]
	
	if contador == 11:	
		try:
			ldr1 = ldr_id.save_value({'value':ldr})
                        hum1 = hum_id.save_value({'value':hum})
                        temp1 = temp_id.save_value({'value':temp})
		except:
			print "DO NOT SEND" 
		contador=0
		contador1=0
		
	if contador2 == 100:	
		arduino.close()
		arduino = serial.Serial('com3',9600)
		contador2=0

	
	print(dato)
	contador=contador+ 1
	contador1=contador1+ 1 
	contador2=contador2+ 1 
