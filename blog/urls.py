from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from home import urls as urlsHome
from posts import urls as urlsPosts
from accounts import urls as urlsAccounts
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(urlsHome)),
    url(r'^posts/', include(urlsPosts, namespace="posts")),
    url(r'^accounts/', include(urlsAccounts, namespace="accounts")),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(
    	regex = r'^media/(?P<path>.*)$',
    	view = serve,
    	kwargs = {'document_root':settings.MEDIA_ROOT}),
]
