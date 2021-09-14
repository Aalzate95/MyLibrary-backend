from django.urls import path, include

urlpatterns = [
        path('libreria/', include('libreria.urls')),
    ]

urlpatterns = [path("api/",include(urlpatterns))]