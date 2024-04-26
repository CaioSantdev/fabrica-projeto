from django.urls import path
from . import views



urlpatterns = [
    path('', views.Dashboard.as_view(),name="home"),
    path('cadastro/', views.Cadastro.as_view(),name="cadastro"),
    path('cursos/', views.Cursos.as_view(),name="cursos"),
    path('listar/', views.Listar.as_view(),name="listar"),
    path('campus/', views.Campus.as_view(),name="campus"),

]