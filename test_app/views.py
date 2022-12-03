from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request->response
# request handler


# def greet(request):
#     return HttpResponse("Hello, Ruth")

def greet(request):
    return render(request, 'test.html', {'name': 'Ruth'}) 

