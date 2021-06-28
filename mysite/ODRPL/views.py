from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import View

#from scraper.SS_scraper import scrape_papers_info
from .scraper import SS_scraper as scrp
#from SS_scraper import scrape_papers_info

import ast, json

def index(request):
	return render(request, "index.html")


def abstracts(request):

	if request.method == "POST":
		query_text = str(request.POST["InputSubject"])

		# clearing extra/duplicate whitespaces
		query_text = " ".join(query_text.split())
		#papers = scrp.scrape_papers_info(query_text)
		request.session["query_text"] = query_text

		file = open("sample.json", "r")
		content = file.read()
		papers = ast.literal_eval(content)
		file.close()

		request.session["papers"] = papers

		context = {
			"query_text": query_text,
			"papers": papers
		}

		return render(request, "abstracts.html", context)

	return HttpResponseRedirect(reverse("index"))


def	full_papers(request):

	if request.method == "POST":
		if request.session.has_key("query_text"):
			query_text = request.session["query_text"]

		if request.session.has_key("papers"):
			papers = request.session["papers"]
		#else:
		#	raise Http404("Error!")

		check_boxes = request.POST.getlist("check")

		if check_boxes:
			chkd_checkboxes_indices = []

			for x in range(len(check_boxes)):
				#remove " from string
				#new_str = check_boxes[x].replace('"', "")
				chkd_checkboxes_indices.append(int(check_boxes[x]))

			print(chkd_checkboxes_indices)
			print(type(papers))

			selected_papers = []

			for x in chkd_checkboxes_indices:
				selected_papers.append(papers[x-1])

			print("\n\n----------------------------------\n\n")
			print(json.dumps(selected_papers, sort_keys=False, indent=4))
			
			context = {
			"query_text": query_text,
			"selected_papers": selected_papers
		}

		return render(request, "full_papers.html", context)
		#return HttpResponse(chkd_checkboxes_indices)



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