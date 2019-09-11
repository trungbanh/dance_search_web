from django.shortcuts import render
from django.http import HttpResponse
from inspect import getmembers
from pprint import pprint
import json


def index(request):
    return render(request, 'query_dance/test.html' )

def dances(request,nameofdance):
    context = {'nameofdance':nameofdance}
    return render(request, 'query_dance/test.html',context )
