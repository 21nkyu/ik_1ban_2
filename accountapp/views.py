from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

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

class AccountCreateview(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'