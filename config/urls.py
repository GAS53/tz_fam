from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="mainapp/")),
    # path("api/", include("mainapp.urls", namespace='api')),

]
