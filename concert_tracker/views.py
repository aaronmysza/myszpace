from django.shortcuts import render


def index(request):
    return render(request, 'concert_tracker/index.html')
