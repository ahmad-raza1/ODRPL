from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def index(request):
	return render(request, 'index.html')

def abstracts(request):
	return render(request, 'abstracts.html')

def loader(request):
	return render(request, 'loader.html')

"""
class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

# Create your views here.

def index(request):
	return HttpResponse("Hello World!")
"""