"""
URL configuration for Api_next project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from userapp.views import*
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',UserRegisterView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('listcreate/',ProductListCreateView.as_view(),name="listcreate"),
    path('retriveupdatedelete/<int:pk>/',ProductretriveupdatedeleteView.as_view(),name="rud"),


]
router = DefaultRouter()
router.register('products',ProductViewset,basename='product')

urlpatterns += router.urls
