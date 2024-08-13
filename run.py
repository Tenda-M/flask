
#.py means it's a python file
import os
import json
from flask import Flask, render_template, request #First, we're importing our Flask class.


app = Flask(__name__)#We're then creating an instance of this and storing it in a variable called 'app'.


@app.route("/") #We're then using the app.route decorator.
#In Python, a decorator starts with the @ symbol, which is also called pie-notation.
#Effectively, a decorator is a way of wrapping functions.
def index(): # this function index returns the "hello world"
    return render_template("index.html")# remember to leave two spaces between python functions


@app.route("/about")
def about():
   data = []
   with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    # ("data/company.json", "r") as json_data: Python is opening the JSON file as "read-only",
    # and assigning the contents of the file to a new variable we've created called json_data.
   return render_template("about.html", page_title="About", company=data) # remember to leave two spaces between python functions


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form["email"])
    return render_template("contact.html", page_title="Contact") # remember to leave two spaces between python functions


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="careers")# remember to leave two spaces between python functions


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)