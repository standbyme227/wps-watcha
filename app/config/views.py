from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def crawler(request):
    return render(request, 'crawler/crawler.html')