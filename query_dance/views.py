from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random 


from .query.test_query import SingletonSparkQL 


def index(request):
    return render(request, 'query_dance/index.html')

def me(request):
    return render(request, 'about_me.html')

@csrf_exempt 
def query(request):
    context = dict()
    if (request.method == 'POST'):

        query_dict = dict(request.POST)
        apsaras = anotation_query_string(query_dict)
        if apsaras == [] :
            # if not found return 00 
            return HttpResponse('00')

        # 34fps and 5s for a video
        # print(apsaras)
        ran = random.randint(1,int(len(apsaras)/2))
        context = int(apsaras[ran].split('_')[1])/170
        context = int(context)
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
    runQuery = SingletonSparkQL.getInstance()
    # print (runQuery)
    apsaras = runQuery.search(query)

    return apsaras
