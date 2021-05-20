from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="post-page"),
    # slug is acctualy a concept of route like = /posts/my-first-post where we can include symbols.
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]