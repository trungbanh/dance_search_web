from django.urls import path 

from . import views

app_name = 'query_dance'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('Apsara',views.query,name = 'Apsara'),
    
]