from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/1")
def work():
    return "hello"
    return "how are you"

@app.route("/workout")
def vada():
    return "workout polam"

@app.route("/hero")
def hero:
return "hero working"


@app.route("/morning")
def morning():
    return "morning hello"

@app.route("/worspace")
def workspace():
    return "worksapce.db"
