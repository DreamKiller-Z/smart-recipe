#!/usr/bin/python
import smbus
import math
import time 
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
# %matplotlib notebook
plt.rcParams['animation.html']='jshtml'
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


#gather 10 times of data

def collecting():
    current_time=0
    x_data = []
    y_data= []

    target = 0
    data = []
    start = time.time()
    ######  collect data once in a while  ####
    fig=plt.figure()
    ax= fig.add_subplot(111)
    fig.show()
    ##########################################
    while(1):
        print("Gyroscope")
        print("--------")
         
        gyroskop_xout = read_word_2c(0x43)
        gyroskop_yout = read_word_2c(0x45)
        gyroskop_zout = read_word_2c(0x47)

        print ("gyroscope_xout: ", ("%5d" % gyroskop_xout), " scale: ", (gyroskop_xout / 131))
        print ("gyroscope_yout: ", ("%5d" % gyroskop_yout), " scale: ", (gyroskop_yout / 131))
        print ("gyroscope_zout: ", ("%5d" % gyroskop_zout), " scale: ", (gyroskop_zout / 131))
        
        print ("Acceleration")
        print ("---------------------")
         
        beschleunigung_xout = read_word_2c(0x3b)
        beschleunigung_yout = read_word_2c(0x3d)
        beschleunigung_zout = read_word_2c(0x3f)

        current_time= current_time+1
        x_data.append(current_time)
        y_data.append(beschleunigung_xout)
        beschleunigung_xout_skaliert = beschleunigung_xout / 16384.0
        beschleunigung_yout_skaliert = beschleunigung_yout / 16384.0
        beschleunigung_zout_skaliert = beschleunigung_zout / 16384.0
         
        print ("accel_xout: ", ("%6d" % beschleunigung_xout), " scale: ", beschleunigung_xout_skaliert)
        print ("accel_yout: ", ("%6d" % beschleunigung_yout), " scale: ", beschleunigung_yout_skaliert)
        print ("accel_zout: ", ("%6d" % beschleunigung_zout), " scale: ", beschleunigung_zout_skaliert)
         
        print ("X Rotation: " , get_x_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))
        print ("Y Rotation: " , get_y_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))

        data.append([gyroskop_xout, gyroskop_yout, gyroskop_zout, beschleunigung_xout, beschleunigung_yout, beschleunigung_zout, target])
        ax.plot(x_data,y_data, color='b')
        time.sleep(0.1)
        print("total time: ", time.time() - start)
        # target += 1

bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect
 
# Aktivieren, um das Modul ansprechen zu koennen
bus.write_byte_data(address, power_mgmt_1, 0)
process = time.time()

collecting()
# try:
#     df_read=pd.read_csv("testdata.csv")
# except pd.io.common.EmptyDataError:
#     data = collecting()
#     df_write = pd.DataFrame(np.array(data), columns=["g_x", "g_y", "g_z", "a_x", "a_y", "a_z"])
#     df_write.to_csv("testdata.csv", index = False)
# except FileNotFoundError:
#     f = open("testdata.csv", "w")
#     data = collecting()
#     df_write = pd.DataFrame(np.array(data), columns=["g_x", "g_y", "g_z", "a_x", "a_y", "a_z"])
#     df_write.to_csv("testdata.csv", index = False)

# try:
#     df_read=pd.read_csv("testdata.csv")
# except FileNotFoundError:
#     f = open("testdata.csv", "w")
# except pd.io.common.EmptyDataError:
#     pass


# count = 0
choose = True
# target = 1
# while(choose):
#
#     print ("---------------------")
#     print("1. collect data \n2. save and end \n3. delete csv \n4. look at testdata.csv")
#     print ("---------------------")
#     answer = input()
#     print(answer)
#     if answer == '1':
#
#         # if (count%2 == 0):
#         #     target = 1
#         # else:
#         #     target = 0
#
#         print("collecting data")
#         data = collecting()
#         df_temp = pd.DataFrame(np.array(data), columns = ["g_x", "g_y", "g_z", "a_x", "a_y", "a_z", "target"])
#         with open("testdata.csv", "a") as f:
#             df_temp.to_csv(f, index =False, header =False)
#         print(df_temp.tail(5))
#
#     elif answer == '2':
#         choose = False
#         print("end")
#     elif answer =='3':
#         os.remove("testdata.csv")
#         print("delete csv")
#         choose = False
#     elif answer =="4":
#         df_read = pd.read_csv("testdata.csv")
#         print(df_read.tail(10))
#         choose =False
