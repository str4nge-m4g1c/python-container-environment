from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "The python app is running..."}
		return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
