from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

from flask import render_template

@app.route("/")
def home():
    return render_template("GUI.py")  
  app.run()
