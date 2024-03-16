from django.urls import path
from myapi import views

urlpatterns = [
   path("fetch-todos", views.alltods),
   path("save-todo", views.savethistodo),
   path("single-todo/<int:id>", views.singlethistodo),
]
