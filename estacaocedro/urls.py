from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.website.urls', namespace='website')),
    url(r'^painel/', include('apps.painel.urls', namespace='painel')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)