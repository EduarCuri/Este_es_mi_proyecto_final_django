"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/', despedida),
    path('saludo_nombre/<nombre>', saludo_nombre),
    path('anio_nacimiento/<anio>', anio_nacimiento),
    path('primer_template/', primer_template),
    path('template_modificado/',template_modificado),
    path('template_modificado2/', template_modificado2),
    path('template_modificado2/<nombre>/<apellido>', template_modificado2),
    path('mostrar_familiares/', mostrar_familiares),
]
