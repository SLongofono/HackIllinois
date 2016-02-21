import os
from flask import Flask
from nocache import nocache
#app = Flask(__name__, static_url_path=os.getcwd())
app = Flask(__name__)


@app.route("/target1.html")
@nocache
def hello():
	command = "python push2html.py 111"
	os.system(command)

	x = open("target1.html", "r")
	page = x.read()
	x.close()
	y = open('log.txt', 'a')
	y.write(page)
	y.write('\n')
	y.close()
	return page

@app.route("/target2.html")
@nocache
def hello2():
	command = "python push2html.py 222"
	os.system(command)

	x = open("target2.html", "r")
	page = x.read()
	x.close()
	y = open('log.txt', 'a')
	y.write(page)
	y.write('\n')
	y.close()
	return page


if __name__ == "__main__":
	app.run()
