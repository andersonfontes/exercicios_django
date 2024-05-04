from django.urls import path
from .views import user_login, user_register, password_reset

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('password-reset/', password_reset, name='password_reset'),
    # Adicione aqui as URLs adicionais, como as páginas de confirmação de email, senha redefinida, etc.
]