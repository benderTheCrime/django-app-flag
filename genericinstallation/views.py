from django.shortcuts import render, HttpResponse
from django_app_flag.decorators import app_flag

@app_flag
def test_page(request):
    return HttpResponse('hi')
