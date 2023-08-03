from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.admin.views.decorators import staff_member_required
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.about, name='about'),   
    path('login/', LoginView.as_view(template_name='home/login.html'), name="login"),
    path('confirm/', views.confirm, name='confirm'),
    path('logout/', LogoutView.as_view(template_name='home/logout.html'), name="logout"),
    path('register/', staff_member_required(views.register_request), name="register"),

]
urlpatterns += staticfiles_urlpatterns()