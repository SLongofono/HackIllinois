import os
from flask import Flask
#app = Flask(__name__, static_url_path=os.getcwd())
app = Flask(__name__)


@app.route("/target1.html")
def hello():
	command = "python ../push2html.py 1"
	os.system(command)

	x = open("../target1.html", "r")
	page = x.read()
	x.close()
	print page
	return page

@app.route("/target2.html")
def hello2():
	command = "python ../push2html.py 0"
	os.system(command)

	x = open("../target2.html", "r")
	page = x.read()
	x.close()
	print page
	return page


if __name__ == "__main__":
	app.run()
