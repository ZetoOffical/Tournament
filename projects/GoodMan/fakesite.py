import requests
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/sort', methods=['POST'])
def sort():
	resp = {'success': True, 'data': sorted(requests.json()['data'], key=lambda x: int(x['_id']))}
	return jsonify(resp)


@app.route('/search', methods=['POST'])
def search():
	pass


@app.route('/parse', methods=['POST'])
def parse():
	pass


if __name__ == '__main__':
	app.run(debug=True)