from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import asyncio


from .query.test_query import SparqlQueries 

def index(request):
    return render(request, 'query_dance/index.html',{'test':123456})

@csrf_exempt 
def query(request):

    context = dict()
    if (request.method == 'POST'):

        query_dict = dict(request.POST)
        # print (query_dict)
        apsaras = anotation_query_string(query_dict)
        context = apsaras
        return HttpResponse(context)

    return render(request, 'query_dance/query.html')
 
def anotation_query_string (query_dict):
    query = ''
    if query_dict['foot'] != ['']:
        query = query+"?Apsara Apsara_v3:hasFootsPosture Apsara_v3:{}. ".format(query_dict['foot'][0])
    if query_dict['hand'] != ['']:
        query = query+'?Apsara Apsara_v3:hasHandRightPosture|Apsara_v3:hasHandLeftPosture Apsara_v3:{}. '.format(query_dict['hand'][0])
    if query_dict['body'] != ['']:
        query = query+'?Apsara Apsara_v3:hasBodyPosture Apsara_v3:{}. '.format(query_dict['body'][0])
    runQuery = SparqlQueries()
    apsaras = runQuery.search(query)

    return apsaras
