from django.shortcuts import render

# Create your views here.
from pip._vendor import requests


def boards_list(request):
    backend_url = "http://127.0.0.1:8000/"
    headers = {'content-type':"application/json"}
    response = requests.get(backend_url,headers=headers)
    boards = response.json()
    return render(request, 'home.html', {'boards': boards['Results']})

def  board_topics(request, board_id):
    pass

