from django.conf.urls import url
from . import views

urlpatterns = [
	url (r'^post_list', views.PostList.as_view(), name="post_list"),
	url (r'^nuevo/$', views.NuevoPost.as_view(), name="nuevo"),
	url (r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detail"),
]