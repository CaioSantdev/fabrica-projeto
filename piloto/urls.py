from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('cadastro/', views.cadastro,name="cadastro"),
    path('cursos/', views.cursos,name="cursos"),
    path('listar/', views.listar,name="listar"),
    path('campus/', views.campus,name="campus"),

]