
#.py means it's a python file
import os
from flask import Flask, render_template #First, we're importing our Flask class.


app = Flask(__name__)#We're then creating an instance of this and storing it in a variable called 'app'.


@app.route("/") #We're then using the app.route decorator.
#In Python, a decorator starts with the @ symbol, which is also called pie-notation.
#Effectively, a decorator is a way of wrapping functions.
def index(): # this function index returns the "hello world"
    return render_template("index.html")# remember to leave two spaces between python functions


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")# remember to leave two spaces between python functions


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="contact")# remember to leave two spaces between python functions


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="careers")# remember to leave two spaces between python functions


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)