from flask import  Flask, render_template, request
from modules import db, Person

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    POST = False
    if request.method == "POST":
        #POST = True
        name = request.form["name"]
        age = request.form["age"]
        male = request.form["male"]
        return render_template("form.html", male=male, name=name, age=age)
    return render_template("home.html", post=POST)



if __name__ == "__main__":
    app.run(debug=True)