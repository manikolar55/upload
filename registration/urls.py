from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('index',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('server_reg',views.server_reg,name='server_reg'),
    path('server_login',views.server_login,name='server_login'),
    path('server_page',views.server_page,name='server_page'),
    path('city',views.city,name='city'),
    path('enter_city',views.enter_city,name='enter_city'),
    path('Edit/<int:id>',views.edit_city,name='edit_city'),
    path('update/<int:id>',views.update_city,name='update_city'),
    path('delete/<int:id>',views.delete_city,name='delete_city'),
    path('country',views.countries,name='countries'),
    path('show_city',views.show_city,name='show_city'),
    path('add/<int:id>',views.add,name='add'),
    path('server_product',views.server_product,name='server_product'),
    path('add_product_server',views.add_product_server,name='add_product_product'),
    path('add_products',views.add_products,name='add_products'),
    path('server_update/<int:id>', views.server_update, name='server_update'),
    path('server_delete/<int:id>', views.server_delete, name='server_delete'),
    path('users_signup', views.users_signup, name='users_signup'),
    # path('success', views.success, name = 'success'),



]
urlpatterns =urlpatterns + static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)