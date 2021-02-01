"""shop URL Configuration

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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from index.views import index, catalog, category1, category2, category3, category4, category5

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), 
    path('admin/', admin.site.urls),
    path('', index),
    path('catalog/', catalog, name='catalog'),
    path('category1/', category1, name='category1'),
    path('category2/', category2, name='category2'),
    path('category3/', category3, name='category3'),
    path('category4/', category4, name='category4'),
    path('category5/', category5, name='category5'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)