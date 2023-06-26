from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("mainapp.urls", namespace='api')),
    # path("", RedirectView.as_view(url="api/")),
    
    

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)