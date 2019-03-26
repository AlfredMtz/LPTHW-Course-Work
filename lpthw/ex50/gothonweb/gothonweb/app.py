from flask import Flask

# Knows how to load .html files out of the templates/ directory
from flask import render_template

app = Flask(__name__, template_folder="templates/")

# My address in the browser ends with this '/', so
# its reference to this section and below function.
@app.route("/")
def index():
    greeting = "that this is a messy world man!"
    scnd_greeting = "just hello world from html code"

    # pass greeting as a variable
    # loads the templates/index.html file and processes it.
    return render_template("foo.html", greeting= greeting)

if __name__ == "__main__":
    app.run(threaded=True) 