from django.http import HttpResponse
from django.shortcuts import render
import json as JSON
import re
from bs4 import BeautifulSoup as bs4
import requests

# Create your views here.
def index(response):
    if response.method == "POST":
        json = JSON.loads(response.POST.get("json"))
        
    else:
        return render(response, 'index.html')

class tasks():
    def sort(response):
        if response.method == "POST":
            json = JSON.loads(response.POST.get("json"))
            return HttpResponse(str(sorted(json['array'],key=lambda k: k['name'],reverse=json['asc'])))
        else:
            return HttpResponse("Вернись на главную страницу!")

    def search(response):
        if response.method == "POST":
            json = JSON.loads(response.POST.get("json"))
            if json['text'] is None:
                return HttpResponse("Ты не указал что-то.")
            elif json['search'] is None:
                return HttpResponse("Ты не указал что-то.")
            if json['exact']:
                text = re.sub(r"\b"+json['search']+r"\b", "<strong>"+json['search']+"</strong>", json['text'])
                return HttpResponse(text)
            else:
                return HttpResponse(json['text'].replace(json['search'], f"<strong>{json['search']}</strong>"))   
    def parse(response):
        if response.method == "POST":
            json = JSON.loads(response.POST.get("json"))
            f = requests.get("https://www.python.org/dev/peps/pep-0008/")
            soup = bs4(f.text,'lxml')
            elem = soup.find(lambda tag: tag.name == "p" and json['search'] in tag.text or tag.name == "h1" and json['search'] in tag.text)
            return HttpResponse(elem)
        else:
            return HttpResponse("Ты куды залез? Иди отсюда.")