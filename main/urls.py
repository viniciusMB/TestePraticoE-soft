from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("consulta/", views.getusers, name="getusers"),
    path("altera/escolha/", views.beforeUpdateUser, name="beforeUpdateUser"),
    path("altera/escolha/<str:pk>/", views.updateUser, name="updateUser"),
]