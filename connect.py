import mysql.connector


from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})



@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
  mydb = mysql.connector.connect(
  host="localhost",
  user="sql-instance-6",
  database="sql-db-2",
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  val = ("square of" num, num**2)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")

	return jsonify({'data': num**2})


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80)




