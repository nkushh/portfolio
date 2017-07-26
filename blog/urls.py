from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
	url(r'^$', views.home, name="blog-home"),
	url(r'^category/(?P<category_id>\d+)/$', views.category_details, name="category-detail"),
	url(r'^post/(?P<post_id>\d+)/$', views.post_details, name="post-detail"),
	url(r'^add-comment/(?P<post_id>\d+)/$', views.add_comment, name="add_comment"),
]