from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello, world";

@app.route("/hello/<user>")
def hello_user(user):
	return "Hello {0}".format(user)
@app.route("/hello/<user>/<year>")
def hello_user_year(user, year):
	return "Тебя зовут {0}, и тебе {1}".format(user, year)


if __name__=="__main__":
	app.run()

