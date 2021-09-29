from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("video", views.video, name="video"),
    path('image', views.image, name = 'image'),
    path('success', views.success, name = 'success'),
    path('images', views.display_images, name = 'images'),
    path('uploadFile', views.uploadfile_view, name ='uploadFile'),
    path('contact_list', views.contact_list_view, name ='contact_list'),
    path('show_contact/<contact_id>', views.show_contact_view, name ='show_contact'),
    path('search', views.search_view, name = 'search'),
]