from django.shortcuts import render, get_object_or_404
from .models import Categorie, Post

# Create your views here.
def home(request):
	context = {
		'categories' : Categorie.objects.all(),
		'posts' : Post.objects.filter(date_published__isnull=False).order_by('-date_published'),
	}
	return render(request, "blog/home.html", context)

def category_details(request, category_id):
	context = {
		'category' : get_object_or_404(Categorie, pk=category_id),
		'categories' : Categorie.objects.all(),
	}
	return render(request, "blog/category_detail.html", context)

def post_details(request, post_id):
	context = {
		'post' : get_object_or_404(Post, pk=post_id),
		'categories' : Categorie.objects.all(),
	}
	return render(request, "blog/post_detail.html", context)
