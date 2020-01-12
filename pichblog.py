from flask import Flask
app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return "Home Page"


@app.route("/about")
def about():
    return "About Page"