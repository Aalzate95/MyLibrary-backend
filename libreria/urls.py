from django.urls import path,include
from rest_framework import routers
from . import views
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'libros',views.LibrosViewSet, basename="libros")

urlpatterns = [
        path('', include(router.urls)),
    ]
