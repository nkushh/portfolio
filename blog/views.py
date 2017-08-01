from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorie, Post, Comment

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
		'posts' : Post.objects.get(category=category_id).filter(date_published__isnull=False).order_by('-date_published'),
	}
	return render(request, "blog/category_detail.html", context)

def post_details(request, post_id):
	context = {
		'post' : get_object_or_404(Post, pk=post_id),
		'categories' : Categorie.objects.all(),
	}
	return render(request, "blog/post_detail.html", context)

def add_comment(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if request.method=="POST":
		author = request.POST['author']
		text = request.POST['text']
		comment = Comment(post=post, author=author, text=text)
		comment.save()
		messages.success(request, 'Success! Your comment has been submitted for approval!')
		return redirect('blog:post-detail', post_id = post_id)
	else:
		return redirect('blog:post-detail', post_id = post_id)
