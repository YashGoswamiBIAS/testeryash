import pyrebase

config = {
  "apiKey": "AIzaSyAcZk0feux91SLAqw1iSvkw66r1Se5IcmA",
  "authDomain": "little-angels-school-5cefc.firebaseapp.com",
  "databaseURL": "https://little-angels-school-5cefc-default-rtdb.firebaseio.com",
  "projectId": "little-angels-school-5cefc",
  "storageBucket": "little-angels-school-5cefc.appspot.com",
  "messagingSenderId": "210531676536",
  "appId": "1:210531676536:web:f802f857035bf58b42988d",
  "measurementId": "G-T5V41GVRMZ"
}

firebase = pyrebase.initialize_app(config=config)
database = firebase.database()
print(dict(database.child("").get().val()))
