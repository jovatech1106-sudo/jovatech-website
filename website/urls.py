from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("contact/", views.contact, name="contact"),
    path("register/", views.student_registration, name="student_registration"),
    path("services/", views.services, name="services"),
    path('courses/', views.courses, name='courses'),
    path('gallery', views.gallery, name='gallery'),
]