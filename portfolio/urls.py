from django.conf.urls import url

from . import views

app_name = 'portfolio'

urlpatterns = [
	url(r'^$', views.index, name="home"),
	url(r'^project/(?P<project_id>\d+)/$', views.project_details, name="project-details"),
	url(r'^facebook/$', views.fb_profile, name="facebook"),
	url(r'twitter/$', views.twitter_profile, name="twitter"),
	url(r'^github/$', views.github_profile, name="github"),
]