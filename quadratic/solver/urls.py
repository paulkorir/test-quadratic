from django.urls import path

from . import views

app_name = 'solver'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # urlconf
]
