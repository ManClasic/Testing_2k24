from django.contrib import admin
from django.urls import path, include
from hola import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', views.principal),
    path('articulos/', include('articulos.urls')),
]
