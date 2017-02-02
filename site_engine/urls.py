from django.conf.urls import url

from . import views

app_name = 'site_engine'

urlpatterns = [
	url(r'^$', views.dashboard, name="dashboard"),
	url(r'^projects/$', views.view_projects, name="view-projects"),
	url(r'^blog-posts/$', views.view_posts, name="view-posts"),
	url(r'^new-project/$', views.new_project, name="new-project"),
	url(r'^blog-categories/$', views.view_blog_categories, name="blog-categories"),
	url(r'^new-blog-category/$', views.new_blog_category, name="new-blog-category"),
]