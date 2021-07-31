from django.http import HttpResponse


def hello_1(request):
    return HttpResponse('hello world!')