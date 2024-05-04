# No arquivo models.py do seu aplicativo de autenticação (accounts)

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione outros campos de perfil, se necessário
