from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login$', views.loginUser, name='login'),
	url(r'^register$', views.register, name='register'),
	#url(r'^show$', views.show, name='show'),
]