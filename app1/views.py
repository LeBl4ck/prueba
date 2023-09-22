from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1Vista1(request):
    html="""
        <h1 style="color:blue">Hola mundo desde app1</h1>
    """
    return HttpResponse(html)

def app1Vista2(request):
    html="""
    <h2 style="color:green">Hola mundo 2 desde app1</h2>
    """
    return Http Response(html)