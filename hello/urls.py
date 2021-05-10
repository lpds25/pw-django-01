from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name="home"),
    path('turma', views.turma_page_view, name="turma"),
    path('<str:name>', views.sauda_page_view, name="sauda"),
]