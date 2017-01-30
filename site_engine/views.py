from django.shortcuts import render
from portfolio.models import Project
from blog.models import Categorie, Post

# Create your views here.
def dashboard(request):
	return render(request, "site_engine/dashboard.html", {})

def view_projects(request):
	context = {
		'projects' : Project.objects.all(),
	}
	return render(request, "site_engine/projects.html", context)

def view_posts(request):
	context = {
		'posts' : Post.objects.all(),
	}
	return render(request, "site_engine/blog_posts.html", context)
