import requests
from flask import Flask, request
from bs4 import BeautifulSoup as BS


app = Flask(__name__)
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}


@app.route('/', methods=['GET'])
def hello_world():
    return 'HELP'


@app.route('/parse', methods=['GET', 'POST'])
def parce():
    search_var = request.args.get('search', default='', type=str)
    if search_var == '':
        return 'meow'
    else:
        r = requests.get('https://www.python.org/dev/peps/pep-0008/', headers=head)
        soup = BS(r.text, 'html.parser')
        out = []

        tegs = [tag.name for tag in soup.html.findAll()]

        all_tegs = []
        for x in tegs:
            if x not in all_tegs:
                all_tegs.append(x)

        for teg in all_tegs:
            teg_info = soup.findAll(teg)
            teg_cont_search = []
            if search_var in str(teg_info):
                teg_cont_search.append()


app.run(host='0.0.0.0')
