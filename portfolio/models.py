from django.db import models

# Create your models here.
class Project(models.Model):
	project_name = models.CharField(max_length=200)
	project_description = models.TextField()
	project_image = models.FileField()
	project_link = models.CharField(max_length=1000)

	def __str__(self):
		return self.project_name
