from django.urls import path
from .views import UsuarioView

urlpatterns=[
    path('usuario/', UsuarioView.as_view(),name='usuario_list'),
    path('usuario/<int:id>', UsuarioView.as_view(), name='usuario_process')
]