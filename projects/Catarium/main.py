from flask import Flask, jsonify, request

app = Flask(__name__)


a_lst = [

]


@app.route('/sort')
def sort():
    b = {
        'asc': request.json['asc'],
        'array': request.json['array']
    }
    c = b['array']
    sort(c, key=lambda x: x['name'])
    print(c)
    return jsonify({'b': {'succes': True, 'array': c}})


app.run(debug=True)