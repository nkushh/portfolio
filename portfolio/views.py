from django.shortcuts import render, get_object_or_404

from .models import Project

# Create your views here.
def index(request):
	context = {
		'projects':Project.objects.all(),
	}
	return render(request, 'home.html', context)

def project_details(request, project_id):
	context = {
		'project' : get_object_or_404(Project, pk=project_id),
		'projects' : Project.objects.all(),
	}
	return render(request, 'portfolio/project.html', context)
