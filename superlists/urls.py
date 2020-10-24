from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from lists import views as list_views
from lists import urls as list_urls  

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),  
]