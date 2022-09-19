from django.http import HttpResponse
from django.shortcuts import render


def helloview(request):
    return HttpResponse('Hello world')
