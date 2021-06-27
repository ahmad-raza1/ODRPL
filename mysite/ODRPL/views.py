from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

#from scraper.SS_scraper import scrape_papers_info
from .scraper import SS_scraper as scrp
#from SS_scraper import scrape_papers_info

def index(request):
	return render(request, 'index.html')


def abstracts(request):

	if request.method == 'POST':
		query_text = str(request.POST['InputSubject'])

		# clearing extra/duplicate whitespaces
		query_text = " ".join(query_text.split())
		papers = scrp.scrape_papers_info(query_text)

		context = {
			"query_text": query_text,
			"papers": papers
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