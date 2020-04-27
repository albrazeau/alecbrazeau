from django.shortcuts import render


def index(request):
    return render(request, 'landingpage.html')


def projects(request):
    return render(request, 'projects.html')


def rivers(request):
    return render(request, 'rivers.html')


def aboutme(request):
    return render(request, 'aboutme.html')
