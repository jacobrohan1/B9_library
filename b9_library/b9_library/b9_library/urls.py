"""
URL configuration for b9_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import welcome_page,show_books, show_single_books, add_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', welcome_page, name = 'home_page'),
    path('show_books/',show_books , name= 'show_books'),
    path('show_single_book/<int:id>/',show_single_books , name= 'show_single_books'),
    path('add_books/',add_books , name= 'add_books'),


]
