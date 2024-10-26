from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404
from django.shortcuts import render

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path('', include('main.urls')),
                   path('accounts/', include('django.contrib.auth.urls')),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


def page_404(request, exception):
    return render(request, 'main/404.html', status=404)


handler404 = page_404
