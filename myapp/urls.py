from django.urls import path
from . import views

# Create own url.
urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.hello),
    path('hello/<int:id>', views.id),
    path('projects', views.projects),
    path('task/<int:id>', views.task)
]