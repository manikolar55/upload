from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('server_reg',views.server_reg,name='server_reg'),
    path('server_login',views.server_login,name='server_login'),
    path('server_page',views.server_page,name='server_page'),
    path('city',views.city,name='city'),
    path('enter_city',views.enter_city,name='enter_city'),
    path('Edit/<int:id>',views.edit_city,name='edit_city'),
    path('update/<str:id>',views.update_city,name='update_city'),
    path('delete/<int:id>',views.delete_city,name='delete_city'),
    path('country',views.countries,name='countries'),


]