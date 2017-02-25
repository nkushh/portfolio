from django.shortcuts import render, redirect, get_object_or_404

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
		'projects' : Project.objects.all().exclude(pk=project_id),
	}
	return render(request, 'portfolio/project.html', context)

def fb_profile(request):
	return redirect("http://www.facebook.com/Piero.muguna.m")

def twitter_profile(request):
	return redirect("http://www.twitter.com/pierombaabu")

def github_profile(request):
	return redirect("http://www.github.com/nkushh")
