from django.shortcuts import render,redirect, get_object_or_404
from portfolio.models import Project
from blog.models import Categorie, Post
from .forms import ProjectForms, CategoryForms

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

def new_project(request):
	if request.method=="POST":

		form = ProjectForms(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=False)
			form.save()
			return redirect("site_engine:view-projects")
	else:
		context = {
			'form' : ProjectForms()
		}
	return render(request, "site_engine/new_project.html", context)

def view_blog_categories(request):
	context = {
		'categories' : Categorie.objects.all(),
	}
	return render(request, "site_engine/blog_categories.html", context)

def new_blog_category(request):
	if request.method=="POST":

		form = CategoryForms(request.POST)
		if form.is_valid():
			form.save()
			return redirect('site_engine:blog-categories')
	else:

		context = {
			'form' : CategoryForms(),
		}
	return render(request, "site_engine/new_blog_category.html", context)
