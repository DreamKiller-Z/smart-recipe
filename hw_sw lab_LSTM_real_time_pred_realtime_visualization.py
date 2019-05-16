# import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy import stats
# import tensorflow as tf
# import seaborn as sns
from pylab import rcParams
# from sklearn import metrics
# from sklearn.model_selection import train_test_split
import matplotlib.animation as animation
import time
import datetime as dt
import pyrebase

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


def data_receiving():
  dataset = db.get().val()
  return dataset


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
xar = []
yar = []
tarr=[]
# t=0
ax=[]
ay=[]
az=[]
def animate(i, xar, yar,ax,ay,az):
    dataset = data_receiving()
    dataset = dataset['dataset']
    dataset = np.asarray(dataset, dtype=np.float32)
    y = dataset[0][0][0]
    ax2=dataset[0][0][3]
    ay1=dataset[0][0][4]
    az1= dataset[0][0][5]
    # xar.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    # xar.append()
    xar.append(dt.datetime.now().strftime('%M:%S:.%f'))
    yar.append(y)
    ax.append(ax2)
    ay.append(ay1)
    az.append(az1)
    #     print(xar,yar)
    xar = xar[-30:]
    yar = yar[-30:]
    ax= ax[-30:]
    ay=ay[-30:]
    az=az[-30:]

    ax1.clear()
    ax1.plot(xar, ax)
    ax1.plot(xar, ay)
    ax1.plot(xar, az)
    # t=t+1
    # print(time.time())
# while (True):

ani = animation.FuncAnimation(fig, animate, fargs=(xar, yar,ax,ay,az), interval=100)
#   print("done")
plt.show()
