import os
from flask import Flask
#app = Flask(__name__, static_url_path=os.getcwd())
app = Flask(__name__)


@app.route("/")
def hello():
	command = "python push2html.py"
	os.system(command)
	x = open("index.html", "r")
	page = x.read()
	x.close()
	print page
	return page

if __name__ == "__main__":
	app.run()
