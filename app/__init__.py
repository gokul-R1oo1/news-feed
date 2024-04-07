from flask import Flask, session

app = Flask(__name__)
app.secret_key = '5H3CRE7K3YTH4T1S16BYT3SL0NG'

from app import views


