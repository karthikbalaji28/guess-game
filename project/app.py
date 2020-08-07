from flask import *
app = Flask(__name__)

a = [[0 for i in range(3)] for j in range(7)];


@app.route("/")
def index():
	return render_template("index.html")
@app.route("/query1" , methods=["POST"])
def query1():
	n = request.form.get("start")
	for i in range(7):
		for j in range(3):
			a[i][j] = (3 * i) + (j + 1) + 10
	return render_template("query1.html" , name = a)
@app.route("/query2" , methods=["POST"])
def query2():
	n = request.form.get("row")
	n = int(n) - 1
	temp = []
	for i in range(7):
		temp.append(a[i][(n + 1) % 3])
	for i in range(7):
		temp.append(a[i][n % 3])
	for i in range(7):
		temp.append(a[i][(n + 2) % 3])
	k = 0
	for i in range(7):
		for j in range(3):
			a[i][j] = temp[k]
			k += 1
	return render_template("query2.html" , name = a)

@app.route("/query3" , methods=["POST"])
def query3():
	n = request.form.get("row")
	n = int(n) - 1
	temp = []
	for i in range(7):
		temp.append(a[i][(n + 1) % 3])
	for i in range(7):
		temp.append(a[i][n % 3])
	for i in range(7):
		temp.append(a[i][(n + 2) % 3])
	k = 0
	for i in range(7):
		for j in range(3):
			a[i][j] = temp[k]
			k += 1
	return render_template("query3.html" , name = a)

@app.route("/output" , methods=["POST"])
def output():
	n = request.form.get("row")
	n = int(n) - 1
	temp = []
	for i in range(7):
		temp.append(a[i][(n + 1) % 3])
	for i in range(7):
		temp.append(a[i][n % 3])
	for i in range(7):
		temp.append(a[i][(n + 2) % 3])
	k = 0
	for i in range(7):
		for j in range(3):
			a[i][j] = temp[k]
			k += 1
	return render_template("output.html" , name = a[3][1])

@app.route("/thank" , methods=["POST"])
def thank():
	n = request.form.get("row")
	if(n == "yes"):
		return render_template("index.html")
	else:
		return render_template("thank.html")

if __name__ == '__main__':
	app.run()

