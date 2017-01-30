from django.conf.urls import url

from . import views

app_name = 'site_engine'

urlpatterns = [
	url(r'^$', views.dashboard, name="dashboard"),
]