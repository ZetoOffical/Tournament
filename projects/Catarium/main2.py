from flask import Flask, jsonify, request

app = Flask(__name__)


a_lst = [

]


@app.route('/search')
def sort():
    if 'ignorecase' not in request.json:
        b = {
            'string': request.json['string'],
            'search': request.json['search'],
            'match': request.json['match'],
        }

    else:
        b = {
            'string': request.json['string'],
            'search': request.json['search'],
            'match': request.json['match'],
            'ignorecase': request.json['ignorecase']
        }
        s1 = b['string']
        s2 = b['search']
        s3 = b['match']
        s4 = b['ignorecase']
        if s4:
            s1 = s1.lower()
        if s3 == 'any':
            r1 = s1.find(s2)
            if r1:
                r2 = r1 + len(s2) - 1
                return jsonify({'success': True, 'data': [r1, r2]})
            else:
                return jsonify({'success': True, 'data': []})
        else:
            if s2 in s1.split():
                r1 = s1.find(s2)
                r2 = r1 + len(s2) - 1
                return jsonify({'success': True, 'data': [r1, r2]})
            else:
                return jsonify({'success': True, 'data': []})


app.run(debug=True)
