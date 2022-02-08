"""ProjectMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from ProjectMusic.views import editar_perfil, login_request, register
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppMusic.urls')),
    path('login', login_request, name= 'login'),
    path('register', register, name='register'),
    path('logout', LogoutView.as_view(template_name = 'AppMusic/logout.html'), name= 'logout'),
    path('user/edit', editar_perfil, name='user_editar')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
