from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("FAQ/", views.FAQ, name="FAQ"),
    path("tutorials/", views.tutorial_list, name="tutorial_list"),
    path("tutorials/<slug:slug>/", views.tutorial_detail, name="tutorial_detail"),
    
    path("robots.txt", views.robots_txt, name="robots_txt"),
]