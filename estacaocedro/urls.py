from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.website.urls', namespace='website')),
    url(r'^painel/', include('apps.painel.urls', namespace='painel')),
]
