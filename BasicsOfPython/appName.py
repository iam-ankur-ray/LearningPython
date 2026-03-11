from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
    return render_template("index.html")

@app.rout("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name","world"))

if __name__ == '__main__':
    app.run()