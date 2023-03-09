from django.urls import path
from web import views

urlpatterns = [
    path('',views.inicio, name="Inicio"), #este era nuestro primer view
    path('pistolas',views.Pistolas,name="pistolas"),
    path('asalto',views.asalto,name="asalto"),
    path('dmr',views.dmr,name="dmr"),
    #path('pistolaformulario/', views.pistolaFormulario,name="pistolaformulario"),
   # path('asaltoformulario/', views.asaltoFormulario,name="asaltoformulario"),
   # path('dmrformulario/', views.dmrFormulario,name="dmrformulario"),
   path('busquedapistola', views.busquedapistola,name="busquedapistola"),
   path('busca/',views.buscar),
    ]