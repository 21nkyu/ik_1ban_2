from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_1, AccountCreateview

app_name = 'accountapp'

urlpatterns = [
    path('overpower/', hello_1, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateview.as_view(), name='create'),

]


