"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This handles the case without a category_slug
    path('<slug:category_slug>/', views.index, name='index_with_category'),  # This handles the case with a category_slug
    path('quotepost/<int:post_id>/', views.quotepost, name='quotepost'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path("about", views.about, name="about"),
]
