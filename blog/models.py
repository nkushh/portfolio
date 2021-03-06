from django.db import models
from django.utils import timezone

# Create your models here.
class Categorie(models.Model):
	category_name = models.CharField(max_length=200)
	created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.category_name

class Post(models.Model):
	category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	post_title = models.CharField(max_length=200)
	post_content = models.TextField()
	post_image = models.FileField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
	date_published = models.DateTimeField(auto_now_add=False, null=True)

	def publish(self):
		self.date_published = timezone.now()
		self.save()

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

	def __str__(self):
		return self.post_title

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments')
	author = models.CharField(max_length=100)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text
