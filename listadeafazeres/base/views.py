from django.http import HttpResponse


def home(response):
    return HttpResponse('<html><body>Olá django</body></html>', content_type='text/html')
