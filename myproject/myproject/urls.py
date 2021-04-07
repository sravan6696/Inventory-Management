from django.conf.urls import url
from django.contrib import admin

from books import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search', views.search, name='search'),
    url(r'^admin/', admin.site.urls),
]