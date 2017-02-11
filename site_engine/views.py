from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from portfolio.models import Project
from blog.models import Categorie, Post
from django.contrib.auth.models import User
from .forms import ProjectForms, CategoryForms, BlogPostForms, UserForms

# Create your views here.
# Function to view the home page dor site_engine app
@login_required
def dashboard(request):
	return render(request, "site_engine/dashboard.html", {})

# BEGIN PORTFOLIO CRUD FUNCTIONS
# Fetches all projects from database
@login_required
def view_projects(request):
	context = {
		'projects' : Project.objects.all(),
	}
	return render(request, "site_engine/projects.html", context)

# Adds a new project to the database and launches form template for the project details
@login_required
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
@login_required
def project_details(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	context = {
		'project' : project,
	}
	return render(request, "site_engine/project_details.html", context)

# Fetches data of a particular project for editing and posts the updated data
@login_required
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
@login_required
def delete_project(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	project.delete()
	return redirect("site_engine:view-projects")

# END PORTFOLIO FUNCTIONS

# BEGIN BLOG CRUD FUNCTIONS
# Fetches all blog categories from teh database
@login_required
def view_blog_categories(request):
	context = {
		'categories' : Categorie.objects.all(),
	}
	return render(request, "site_engine/blog_categories.html", context)

# Adds a new blog category to the database and launches the form for the category details
@login_required
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
@login_required
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
@login_required
def blog_category_details(request, category_id):
	category = get_object_or_404(Categorie, pk=category_id)
	context = {
		'category' : category,
	}
	return render(request, "site_engine/blog_category_details.html", context)

@login_required
def delete_blog_category(request, category_id):
	category = get_object_or_404(Categorie, pk=category_id)
	category.delete()
	return redirect("site_engine:blog-categories")

# Fetches all the blog posts in the database
@login_required
def view_posts(request):
	context = {
		'posts' : Post.objects.all().order_by('-date_created'),
	}
	return render(request, "site_engine/blog_posts.html", context)

# Function to get published blogs only
@login_required
def published_blog_posts(request):
	context = {
		'posts' : Post.objects.filter(date_published__isnull=False).order_by('-date_published'),
	}
	return render(request, "site_engine/blog_posts.html", context)

# Function to get draft blogs only
@login_required
def draft_blog_posts(request):
	context = {
		'posts' : Post.objects.filter(date_published__isnull=True).order_by('-date_created'),
	}
	return render(request, "site_engine/blog_posts.html", context)

# Function to get blog post details
@login_required
def post_details(request, post_id):
	context = {
		'post' : get_object_or_404(Post, pk=post_id)
	}
	return render(request, "site_engine/post_details.html", context)

# Function to publish a draft post
@login_required
def publish_blog_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.publish()
	return redirect("site_engine:post-details", post_id=post_id)

@login_required
def new_blog_post(request):
	if request.method=="POST":
		form = BlogPostForms(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("site_engine:view-posts")
	else:
		context = {
			'form' : BlogPostForms(),
		}
	return render(request, "site_engine/new_blog_post.html", context)

@login_required
def update_blog_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if request.method=="POST":
		form = BlogPostForms(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
			return redirect("site_engine:post-details", post_id=post_id)
	else:
		context = {
			'form' : BlogPostForms(instance=post),
			'post' : post,
		}
	return render(request, "site_engine/edit_blog_post.html", context)

@login_required
def delete_blog_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.delete()
	return redirect("site_engine:view-posts")
# END BLOG FUNCTIONS

# START USERS FUNCTIONS
@login_required
def view_users(request):
	context = {
		'users' : User.objects.all(),
	}
	return render(request, "site_engine/users.html", context)

@login_required
def new_user(request):
	if request.method=="POST":
		form = UserForms(request.POST)
		if form.is_valid():
			form.save()
			return redirect("site_engine:users")
	else:
		context = {
			'form' : UserForms(),
		}
	return render(request, "site_engine/new_user.html", context)
