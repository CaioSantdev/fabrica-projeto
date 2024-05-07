from django.urls import path
from piloto.views import DashboardView, DashboardView, DashboardView, DashboardView

urlpatterns = [
    path('', DashboardView.as_view(),name="home"),
    path('cadastro/', views.CadastroView.as_view(),name="cadastro"),
    path('cursos/', views.CursosView.as_view(),name="cursos"),
    path('listar/', views.ListarView.as_view(),name="listar"),
    path('campus/', views.CampusView.as_view(),name="campus"),
    path('editar-estudante/<uuid:pk>/', views.EditarEstudanteView.as_view(),name="editarEstudante"),
    path('apagar-estudante/<int:estudante_id>/', views.ApagarEstudanteView.as_view(),name="apagarEstudante"),

]