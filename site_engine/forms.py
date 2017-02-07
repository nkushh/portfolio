from django import forms

from portfolio.models import Project
from blog.models import Categorie, Post

class ProjectForms(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['project_name', 'project_description', 'project_image', 'project_link']

class CategoryForms(forms.ModelForm):
	class Meta:
		model = Categorie
		fields = ['category_name']

class BlogPostForms(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('category', 'post_title', 'post_content', 'post_image')