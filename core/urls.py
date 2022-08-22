from django.urls import path
from core import views

urlpatterns = [
  
    path('about/',views.aboutpage,name='about'),
    path('gallery/',views.gallerypage,name='gallery'),
    path('contact/',views.contactpage,name='contact'),
]
