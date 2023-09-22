from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2Vista1(request):
    html="""
        <h3 style="color:yellow">Hola mundo desde app1</h3>
    """
    return HttpResponse(html)

def app2Vista2(request):
    html="""
    <h4 style="color:red">Hola mundo 2 desde app1</h4>
    """
    return HttpResponse(html)