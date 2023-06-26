from django.urls import path
from mainapp import views


app_name = 'mainapp'

urlpatterns = [
    path('clients/create/', views.RegisterView.as_view(), name='create_user')

    ]
