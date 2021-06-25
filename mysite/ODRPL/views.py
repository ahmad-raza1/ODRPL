from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

def index(request):
	return render(request, 'index.html')


def abstracts(request):

	if request.method == 'POST':
		query_text = str(request.POST['InputSubject'])

		# clearing extra/duplicate whitespaces
		query_text = " ".join(query_text.split())

		context = {
			"query_text": query_text,
			"size": 10
		}

		return render(request, 'abstracts.html', context)


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