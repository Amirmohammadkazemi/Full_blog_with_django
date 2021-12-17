from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('blogs/', views.Blogs),
    path('projects', views.Projects),
    path('contact', views.Contact),
    path('support', views.Support),
    path('aboutme', views.AboutMe),
]