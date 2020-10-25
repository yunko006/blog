from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    # Page for each blog post
    path("<int:post_id>/", views.post, name="post"),
    # Page to create a new post
    path("new_post/", views.new_post, name="new_post"),
    # Page to edit one post
    path("edit_entry/<int:post_id>/", views.edit_entry, name="edit_entry"),
    # Page to delete a post
    path("delete_post/<int:post_id>/", views.delete_post, name="delete_post"),
]
