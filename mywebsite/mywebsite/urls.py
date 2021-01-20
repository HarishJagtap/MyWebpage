from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from main.views import home_view
from main.views import response_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = response_404
