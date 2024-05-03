from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(),name="home"),
    path('cadastro/', views.CadastroView.as_view(),name="cadastro"),
    path('cursos/', views.CursosView.as_view(),name="cursos"),
    path('listar/', views.ListarView.as_view(),name="listar"),
    path('campus/', views.CampusView.as_view(),name="campus"),
    path('editar-estudante/<int:estudante_id>/', views.EditarEstudanteView.as_view(),name="editarEstudante"),
    path('apagar-estudante/<int:estudante_id>/', views.ApagarEstudanteView.as_view(),name="apagarEstudante"),

]