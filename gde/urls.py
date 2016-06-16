"""gde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from app.views import categoria
from app.views import categorias_list
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^login/$', auth_views.login, {'template_name': 'login.html'}),
                  url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}),
                  url(r'^categoria/$', categoria),
                  url(r'^categorias_list/$', categorias_list),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
