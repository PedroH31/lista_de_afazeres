from django.urls import path

from listadeafazeres.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
