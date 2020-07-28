import requests
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/sort', methods=['POST'])
def sort():
	resp = {'success': True, 'data': sorted(requests.json()['data'], key=lambda x: int(x['_id']))}
	return jsonify(resp)


if __name__ == '__main__':
	app.run(debug=True)
