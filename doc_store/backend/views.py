from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'message': "Hello, world. You're at the backend index."}
    return render(request, 'test.html', context)
