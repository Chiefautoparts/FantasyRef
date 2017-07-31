from django.conf.urls import url
from . import views


app_name='refs'
urlpatterns = [
	url(r'^home$', views.home, name="home"),
	url(r'^refMaker$', views.refMaker, name="refMaker"),
]