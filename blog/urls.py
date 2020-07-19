from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="blog.home"),
    path('blog/', views.blog_view, name="blog.blog")
]
