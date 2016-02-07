from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, engineers! You're at the logic world.")
