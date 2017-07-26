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
	url(r'^published-posts/$', views.published_blog_posts, name="published-posts"),
	url(r'^draft-posts/$', views.draft_blog_posts, name="draft-posts"),
	url(r'^post/(?P<post_id>\d+)/detail/$', views.post_details, name="post-details"),
	url(r'^new-post/$', views.new_blog_post, name="new-post"),
	url(r'^publish-post/(?P<post_id>\d+)/$', views.publish_blog_post, name="publish-post"),
	url(r'^edit-post/(?P<post_id>\d+)/$', views.update_blog_post, name="edit-post"),
	url(r'^delete-post/(?P<post_id>\d+)/$', views.delete_blog_post, name="delete-post"),
	url(r'^comments/$', views.posts_comments, name="view-comments"),
	url(r'^approve-comment/(?P<comment_id>\d+)/$', views.approve_comment, name="approve-comment"),
	url(r'^delete-comment/(?P<comment_id>\d+)/$', views.delete_comment, name="delete-comment"),
	url(r'^users/$', views.view_users, name="users"),
	url(r'^new-user/$', views.new_user, name="new-user"),
]