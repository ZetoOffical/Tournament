from flask import Flask, request, jsonify

import bs4
import requests


app = Flask(__name__)


@app.route('/sort', methods=['POST'])
def _sort():
    json_ = request.json
    needed_list = json_['array']
    r_needed_list = sorted(needed_list, key=lambda k: int(k['_id']))
    response = {
        "success": True,
        "data": r_needed_list
    }
    return jsonify(response)


@app.route('/search', methods=['POST'])
def search():
    # Я вообще не понял, что должен делать match: exact, так что его не могу реализовать.
    json_ = request.json
    if 'match' not in json_.keys():
        json_['match'] = 'any'
    if 'ignorecase' not in json_.keys():
        json_['ignorecase'] = True
    resp_list = [0]
    if json_['match'] == 'any':
        r_search = json_['search']
        r_string = json_['string']
        if json_['ignorecase']:
            r_search = str(json_['search']).lower()
            r_string = str(json_['string']).lower()
        continue_ = True
        while continue_:
            if not r_string.find(r_search, resp_list[-1]):
                continue_ = False
                break
            resp_list.append(r_string.find(r_search, resp_list[-1]))
        resp_list.pop(0)
    return jsonify(
        {
            "success": True,
            "data": resp_list
        }
    )


@app.route('/parse', methods=['GET'])
def parse():
    search_ = ''
    if 'search' in request.args.keys():
        search_ = request.args['search']
    resp = requests.get('https://www.python.org/dev/peps/pep-0008/')
    str_results = ''
    if not search_:
        results = {}
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        for tr in soup.find_all('tr', {'class': 'field'}):
            key = tr.find('th').get_text()
            val = tr.find('td').get_text()
            results[key] = val
        for k, v in results.items():
            str_results += f'{k}: {v}'
    return jsonify(
        {
            "success": True,
            "data": str_results
        }
    )


if __name__ == '__main__':
    app.run(debug=True)

