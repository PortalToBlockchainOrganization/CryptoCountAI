from django.http import HttpResponse

def hello_world(request):
    print("Hello, world!")
    return HttpResponse("Hello, world!")




