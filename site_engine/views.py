from django.shortcuts import render,redirect, get_object_or_404
from portfolio.models import Project
from blog.models import Categorie, Post
from .forms import ProjectForms, CategoryForms

# Create your views here.
# Function to view the home page dor site_engine app
def dashboard(request):
	return render(request, "site_engine/dashboard.html", {})

# BEGIN PORTFOLIO CRUD FUNCTIONS
# Fetches all projects from database
def view_projects(request):
	context = {
		'projects' : Project.objects.all(),
	}
	return render(request, "site_engine/projects.html", context)

# Adds a new project to the database and launches form template for the project details
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

# Fetches details of a particular project from the database 
def project_details(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	context = {
		'project' : project,
	}
	return render(request, "site_engine/project_details.html", context)

# Fetches data of a particular project for editing and posts the updated data
def edit_project(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if request.method=="POST":
		form = ProjectForms(request.POST, request.FILES, instance=project)
		if form.is_valid():
			form.save()
			return redirect("site_engine:project-details", project_id=project_id)
	else:
		form = ProjectForms(instance=project)
	return render(request, "site_engine/edit_project.html", {'form':form})

# Deletes a particular project from the database
def delete_project(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	project.delete()
	return redirect("site_engine:view-projects")

# END PORTFOLIO FUNCTIONS

# BEGIN BLOG CRUD FUNCTIONS
# Fetches all blog categories from teh database
def view_blog_categories(request):
	context = {
		'categories' : Categorie.objects.all(),
	}
	return render(request, "site_engine/blog_categories.html", context)

# Adds a new blog category to the database and launches the form for the category details
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

# Fetches details of a particular blog category for editing and launches the form  for the same
def edit_blog_category(request, category_id):
	category = get_object_or_404(Categorie, pk=category_id)
	if request.method=="POST":
		form = CategoryForms(request.POST, instance=category)
		if form.is_valid():
			form.save()
			return redirect("site_engine:blog-categories")
	else:
		context = {
			'form' : CategoryForms(instance=category)
		}
	return render(request, "site_engine/edit_blog_category.html", context)

# Fetches a particular blog category and its details from the database
def blog_category_details(request, category_id):
	category = get_object_or_404(Categorie, pk=category_id)
	context = {
		'category' : category,
	}
	return render(request, "site_engine/blog_category_details.html", context)

def delete_blog_category(request, category_id):
	category = get_object_or_404(Categorie, pk=category_id)
	category.delete()
	return redirect("site_engine:blog-categories")

# Fetches all the blog posts in teh database
def view_posts(request):
	context = {
		'posts' : Post.objects.all(),
	}
	return render(request, "site_engine/blog_posts.html", context)
# END BLOG FUNCTIONS
