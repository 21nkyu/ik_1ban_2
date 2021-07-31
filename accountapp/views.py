from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import accapp_HelloWorld


def hello_1(request):
    if request.method == 'POST':

        temp = request.POST.get('hello_1_input')

        new_hello_1 = accapp_HelloWorld()
        new_hello_1.text = temp
        new_hello_1.save()


        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_1_list = accapp_HelloWorld.objects.all()
        return render(request, 'accountapp/overpower.html', context={'hello_1_list': hello_1_list})
