from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('Destinos/', views.Destinos, name='Destinos'),
    path('Pasajes/', views.Pasajes, name='Pasajes'),
    path('lista/', views.ReservaListView.as_view(), name='reserva_list'),
    path('<int:pk>/', views.ReservaDetailView.as_view(), name='reserva_detail'),
]
    
    

urlpatterns+=[
    path('create/', views.ReservaCreate.as_view(), name= 'reserva_create'),
    path('lista/<int:pk>/update/',views.ReservaUpdate.as_view(), name='reserva_update'),
    path('lista/<int:pk>/delete/',views.ReservaDelete.as_view(), name='reserva_delete'),
]   