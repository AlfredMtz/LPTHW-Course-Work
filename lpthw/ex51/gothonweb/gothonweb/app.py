
# imports the Flask class
from flask import Flask
# module to render app code in the web
from flask import render_template
# module that request things from the browser
from flask import request
import os
# variable app becomes an instance of the Flask class
app = Flask(__name__, template_folder="templates/")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# route() decorator tells Flask what URL should trigger our function, but
# first pass a form('POST' or 'GET' type) to collect data from the user 
# and then run this data to this application.
@app.route("/hello", methods=['POST', 'GET'])
# Once we found weather the form is either under a 'POST' or 'GET' method,
# we can run the index() function.
def index():
    greeting = "Hello World"
    # Process the form as if it were filled out and submitted, returning the
    # proper greeting.
    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet},{name}"
        return render_template("index.html", greeting=greeting)
    # Else if the method is 'GET' or anything else, it simply
    # returns the from again to keep filling it out over and over again.
    else:
        return render_template("hello_form.html")


# if URL ends in /hello2,then do as said in the next function
@app.route("/hello2", methods=['POST', 'GET'])
def hello2():
    return render_template("index_laid_out.html", greeting="Nothing")


#Specify the root (ex: test.com/upload)
@app.route("/")

def ind():
    return render_template("fileupload_form.html")



@app.route("/upload", methods=['POST'])
# When the user submit the buttom, we want to upload the files
# to a given path
def upload():
    # join or add to this path a folder
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    # if folder 'images/' does not exist in this path
    if not os.path.isdir(target):
        os.mkdir(target)

    # Since we allowed multiple files in the fileupload form then
    # we need to loop through the files.
    # request.files.getlist("file") --> returns a list of files' names
    # Then for file in this list do the next
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
    # now tell the server to upload this specific file to this location
    # with this specific names
    # We are adding the [filename] to the [target] folder.
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")

    
if __name__ == "__main__":
    app.run()
