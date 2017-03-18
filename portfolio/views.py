from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail

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

def send_email(request):
	if request.method=="POST":
		subject = 'Email From Portfolio Site'
		name = request.POST['name']
		emailFrom = request.POST['email']
		content = request.POST['message']
		message = '%s \nFrom: %s \n%s' % (content, name, emailFrom)
		emailTo = [settings.EMAIL_HOST_USER]

		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
		success = "Message successfully sent"
		context = {
			success : success,
		}
		return redirect('portfolio:home')

def fb_profile(request):
	return redirect("http://www.facebook.com/Piero.muguna.m")

def twitter_profile(request):
	return redirect("http://www.twitter.com/pierombaabu")

def github_profile(request):
	return redirect("http://www.github.com/nkushh")
