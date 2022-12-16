from django.urls import path
from . import views

# Create own url.
urlpatterns = [
    path('', views.hello),
]