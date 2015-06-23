"""callhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", "ivr.views.home", name="home"),
    url(r"^register/", "ivr.views.register", name="register"),
    url(r"^login/", "ivr.views.login", name="login"),
    url(r"^signout/", "ivr.views.signout", name="signout"),
    url(r"^request/config_ivr/", "ivr.views.config_ivr", name="config_ivr"),
    url(r"^request/ivr/edit/(?P<ivr_id>[0-9])/(?P<user_id>[0-9])", "ivr.views.ivr_edit", name="ivr_edit"),
    # url(r"^response/ivr/", "ivr.views.ivr_view", name="ivr_view"),
    # url(r"^response/ivr/(?P<ivr_id>\w+)/(?P<user_id>\w+)", "ivr.views.ivr_endpoint", name="ivr_endpoint"),
    url(r"^response/ivr/list/" , "ivr.views.ivrs", name="ivrs"),
    url(r"^response/ivr/delete/(?P<ivr_id>[0-9])/(?P<user_id>[0-9])/", "ivr.views.ivr_delete", name="ivr_delete"),
    
    # (?P<user_id>\w+)
    #url(r"^contact/$", "ivr.views.contact", name="contact")

    url(r'^api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)