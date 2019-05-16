import pyrebase

config = {
    "apiKey": "AIzaSyDIAFBwmKmGt-B2RPBcl-ZjHuRGo-R1JZ0",
    "authDomain": "gix-510.firebaseapp.com",
    "databaseURL": "https://gix-510.firebaseio.com",
    "storageBucket": "gix-510.appspot.com",
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

dataset = db.get(dataset)

print(dataset)
