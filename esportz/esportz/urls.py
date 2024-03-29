"""esportz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from App.views import *

admin.site.site_header = 'Esportz'
admin.site.site_title = 'Site'
admin.site.index_title= 'Esportz Administration'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', submit),
    path('excel', excel),
    path('email', email),
    path('fifa_submit', fifa_submit),
    path('fifa_excel', fifa_excel),
    path('valo_submit', valo_submit),
    path('valo_excel', valo_excel),
]
