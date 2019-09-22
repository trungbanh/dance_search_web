from django.shortcuts import render
from django.http import HttpResponse
from inspect import getmembers
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt

import json


def index(request):
    return render(request, 'query_dance/index.html')

@csrf_exempt 
def query(request):
    # print (request.method)
    if (request.method == 'POST'):
        print(request.POST)
        print(request.POST['body'])
        print(request.POST['hand'])

    return render(request, 'query_dance/query.html')
