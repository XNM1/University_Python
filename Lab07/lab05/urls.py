"""lab05 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from atmomodule import views

urlpatterns = [
    path('', views.index),
    path('sensors/', views.sensors),
    path('sensor/create/', views.SensorCreateView.as_view()),
    path('sensor_category/create/', views.SensorCategoryCreateView.as_view()),
    path('snapshot/create/', views.AtmoSnapshotCreateView.as_view()),
    re_path(r'^success/(?P<data>\D+)/', views.success),
    path('exports/', views.exports),
    path('exports/xml/', views.export_xml),
    path('exports/docx/', views.export_docx),
    path('data/xml/', views.get_xml),
    path('data/docx/', views.get_docx),
    path('admin/', admin.site.urls),
    re_path(r'^sensors/(?P<id>\d+)/', views.sensor),
]
