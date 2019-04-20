from django.shortcuts import render
from django.http import HttpResponse
def showResult(request):
    s="Bahoot hard"
    return HttpResponse(s)
def showTest(request):
    s='howwegd????'
    return HttpResponse(s)
