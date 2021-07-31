from django.urls import path

from accountapp.views import hello_1

app_name = 'accountapp'

urlpatterns = [
    path('overpower/', hello_1, name='hello world')

]


