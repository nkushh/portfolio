from django.conf.urls import url

from . import views

app_name = 'site_engine'

urlpatterns = [
	url(r'^$', views.dashboard, name="dashboard"),
	url(r'^projects/$', views.view_projects, name="view-projects"),
	url(r'^blog-posts/$', views.view_posts, name="view-posts"),
]