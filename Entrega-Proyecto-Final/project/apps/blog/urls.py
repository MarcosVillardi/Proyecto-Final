from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='index'),
    path('registrar_garaje/', views.registrar_garaje, name='registrar_garaje'),
    path('reserva_list/', views.Reserva_list.as_view(), name='reserva_list'),
    path('reserva_create/',staff_member_required( views.Reserva_create.as_view()), name='reserva_create'),
    # se que estos 2 urls deben incluir el pk pero al ponerlo no deja ingresar a la pagina en cuestion asi que prefiero comentarlos
#    path('reserva_delete/<int:pk>',staff_member_required( views.Reserva_delete.as_view()), name='reserva_delete'),
#    path('reserva_update/<int:pk>', staff_member_required(views.Reserva_update.as_view()), name='reserva_update'),
    path('reserva_delete/',staff_member_required( views.Reserva_delete.as_view()), name='reserva_delete'),
    path('reserva_update/', staff_member_required(views.Reserva_update.as_view()), name='reserva_update'),
    path('reserva_index', views.reserva_index, name='reserva_index'),
    path('garaje_list/', views.Garaje_list.as_view(), name='garaje_list'),
    path('garaje_create/', staff_member_required(views.Garaje_create.as_view()), name='garaje_create'),
    # se que estos 2 urls deben incluir el pk pero al ponerlo no deja ingresar a la pagina en cuestion asi que prefiero comentarlos
#    path('garaje_delete/<int:pk>', views.Garaje_delete.as_view(), name='garaje_delete'),
#    path('garaje_update/<int:pk>', views.Garaje_update.as_view(), name='garaje_update'),
    path('garaje_delete/', staff_member_required(views.Garaje_delete.as_view()), name='garaje_delete'),
    path('garaje_update/', staff_member_required(views.Garaje_update.as_view()), name='garaje_update'),
    path('garaje_index', views.garaje_index, name='garaje_index'),

]
urlpatterns += staticfiles_urlpatterns()