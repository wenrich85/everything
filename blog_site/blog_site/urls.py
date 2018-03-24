"""blog_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from blog.views import PostListView, model_form_upload, PostDetailView, CategoryListView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', PostListView.as_view(), name='home'),
    re_path(r'^(?P<pk>[\d]+)/$', PostDetailView.as_view(), name='detail'),
    re_path(r'^(?P<category>[-\w]+)/$', CategoryListView.as_view(), name='category'),
    re_path(r'^uploads/form/$', model_form_upload, name='model_form_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
