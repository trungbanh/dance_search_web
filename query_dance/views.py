from django.shortcuts import render
from django.http import HttpResponse
from inspect import getmembers
from pprint import pprint
import json


def index(request):
    return render(request, 'query_dance/index.html')

def query(request):
    return render(request, 'query_dance/query.html')
