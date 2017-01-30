from django.shortcuts import render
from portfolio.models import Project

# Create your views here.
def dashboard(request):
	return render(request, "site_engine/dashboard.html", {})

def view_projects(request):
	context = {
		'projects' : Project.objects.all(),
	}
	return render(request, "site_engine/projects.html", context)
