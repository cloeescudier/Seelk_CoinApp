"""
Definition of urls for CoinApp.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework import routers
admin.autodiscover()

from django.urls import path
from django.conf.urls import include

from app.urls import router as app_router

router = routers.DefaultRouter()
router.registry.extend(app_router.registry)

urlpatterns = [
    # Examples:
    # url(r'^$', CoinApp.views.home, name='home'),
    # url(r'^CoinApp/', include('CoinApp.CoinApp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    path("admin/", admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include(router.urls))
]
