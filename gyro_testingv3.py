import smbus
import math
import time 
# import pandas as pd
# import numpy as np
import os
import pyrebase
from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

config = {

    "apiKey": "AIzaSyDIAFBwmKmGt-B2RPBcl-ZjHuRGo-R1JZ0",
    "authDomain": "gix-510.firebaseapp.com",
    "databaseURL": "https://gix-510.firebaseio.com",
    "projectId": "gix-510",
    "storageBucket": "gix-510.appspot.com",
    "messagingSenderId": "721539835802"
  }
firebase = pyrebase.initialize_app(config)

auth= firebase.auth();
# user= auth.sign_in_anonymous();	

db = firebase.database()
#accelorometer and gyroscope data collecting
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(reg):
    return bus.read_byte_data(address, reg)
 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

#writing collected data into a 3d array

def collecting():
    # target = 0
    # output = []
    dataset = []
    
    ######  collect data once in a while  ####

    ##########################################
    flag = True
    while(flag):
    	time.sleep(0.2)
    	# start = time.time()
    	gyroskop_xout = read_word_2c(0x43)
    	gyroskop_yout = read_word_2c(0x45)
    	gyroskop_zout = read_word_2c(0x47)
    	beschleunigung_xout = read_word_2c(0x3b)
    	beschleunigung_yout = read_word_2c(0x3d)
    	beschleunigung_zout = read_word_2c(0x3f)
    	# start=time.time()
    	# print("time for each update: ", time.time() - start)
    	# beschleunigung_xout_skaliert = np.divide(beschleunigung_xout , 16384.0)
    	# beschleunigung_yout_skaliert = np.divide(beschleunigung_yout , 16384.0)
    	# beschleunigung_zout_skaliert = np.divide(beschleunigung_zout , 16384.0)

    	beschleunigung_xout_skaliert = beschleunigung_xout/16384.0
    	beschleunigung_yout_skaliert = beschleunigung_yout/16384.0
    	beschleunigung_zout_skaliert = beschleunigung_zout/16384.0

    	# gy_x = np.divide(gyroskop_xout , 131)
    	# gy_y = np.divide(gyroskop_yout , 131)
    	# gy_z = np.divide(gyroskop_zout , 131)

    	gy_x = gyroskop_xout/131
    	gy_y = gyroskop_yout/131
    	gy_z = gyroskop_zout/131

    	# print("time for each update: ", time.time() - start)
    	
    	data = [gy_x, gy_y, gy_z, beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert]
    	
    	dataset.append(data)
    	start=time.time()
    	if len(dataset)>10:
    		dataset.pop(0)
    		db.update({"dataset": [dataset]})
    	print("time for each update: ", time.time() - start) 
    	# r = requests.post("http://205.175.106.102:5000/", json={"data":dataset})

    return dataset


bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect
 
# Aktivieren, um das Modul ansprechen zu koennen
bus.write_byte_data(address, power_mgmt_1, 0)
process = time.time()

# r = requests.post("http://10.18.242.64:8080/", json={"test":"testing"})

while(True):
	dataset = collecting()

	# db.update({"dataset": [dataset]})




		




