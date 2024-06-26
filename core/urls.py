"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicos.urls')),  # Inclui as URLs do seu aplicativo
]  


# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ou
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#     Essa configuração verifica se o modo de depuração (DEBUG) está ativado no arquivo settings.py antes de adicionar as URLs para servir arquivos estáticos. Isso garante que os arquivos estáticos sejam servidos apenas durante o desenvolvimento quando DEBUG estiver definido como True.
