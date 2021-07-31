from django.http import HttpResponse
from django.shortcuts import render


def hello_1 (request):
    if request.method == 'POST':
        return render(request, 'accountapp/overpower.html', context={'text':'POST'})
    else:
        return render(request, 'accountapp/overpower.html', context={'text': 'GET'})
