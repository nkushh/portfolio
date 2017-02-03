from django.conf.urls import url

from . import views

app_name = 'site_engine'

urlpatterns = [
	url(r'^$', views.dashboard, name="dashboard"),
	url(r'^projects/$', views.view_projects, name="view-projects"),
	url(r'^new-project/$', views.new_project, name="new-project"),
	url(r'^project-details/(?P<project_id>\d+)/$', views.project_details, name="project-details"),
	url(r'^edit-project/(?P<project_id>\d+)/$', views.edit_project, name="edit-project"),
	url(r'^delete-project/(?P<project_id>\d+)/$', views.delete_project, name="delete-project"),
	url(r'^blog-categories/$', views.view_blog_categories, name="blog-categories"),
	url(r'^new-blog-category/$', views.new_blog_category, name="new-blog-category"),
	url(r'^blog-category-details/(?P<category_id>\d+)/$', views.blog_category_details, name="blog-category-details"),
	url(r'^edit-blog-category/(?P<category_id>\d+)/$', views.edit_blog_category, name="edit-blog-category"),
	url(r'^delete-blog-category/(?P<category_id>\d+)/$', views.delete_blog_category, name="delete-blog-category"),
	url(r'^blog-posts/$', views.view_posts, name="view-posts"),
]