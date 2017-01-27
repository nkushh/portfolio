from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
	url(r'^$', views.home, name="blog-home"),
	url(r'^post/(?P<post_id>\d+)/$', views.post_details, name="post-detail"),
]