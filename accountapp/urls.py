from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_1, AccountCreateview, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns = [
    path('overpower/', hello_1, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateview.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update')

]


