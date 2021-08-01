from django.urls import path

from profileapp.views import ProfileCreateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create')

]

# (경로/ - 로직 -라우팅이름)