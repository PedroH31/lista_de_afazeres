from django.http import HttpResponse


def home(response):
    return HttpResponse('Olá django')
