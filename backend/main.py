from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)

CORS(app)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("./little-angels-school-5cefc-firebase-adminsdk-lf3xq-3f93d9b270.json")
firebase_admin.initialize_app(cred,{
  "databaseURL" : "https://little-angels-school-5cefc-default-rtdb.firebaseio.com/"
})

ref = db.reference("/")



@app.route("/api")
@cross_origin()
def api():
    return ref.get()


if __name__ == "__main__":
    app.run()