import json
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort():
	a = {'success': True,
    'data': [{"_id": "80808080", "name": "Anton"}, {"_id": "90909090", "name": "Gosha"}]}
	resp = {'success': True, 'data': sorted(a['data'], key=lambda x: int(x['_id']))}
	return jsonify(resp)

@app.route('/search', methods=['POST'])
def search():
	pass

@app.route('/parse', methods=['POST'])
def parse():
	pass

if __name__ == '__main__':
	app.run(debug=True)