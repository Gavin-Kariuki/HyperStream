from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("<int:id>/delete", views.delete_post, name = "delete_post"),
    path("new_post/", views.new_post, name = "new_post"),
    path("<int:pk>/", views.post_detail, name = "post_detail"),
    path("<int:pk>", views.like, name = "likes"),
]