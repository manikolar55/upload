from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('index',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('server_reg',views.server_reg,name='server_reg'),
    # path('server_login',views.server_login,name='server_login'),
    path('server_page',views.server_page,name='server_page'),
    path('admin_user',views.admin_user,name='admin_user'),
    path('admin_showServiceProvider',views.admin_showServiceProvider,name='admin_showServiceProvider'),
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
    path('user_product', views.user_product, name='user_product'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('server_logout', views.server_logout, name='server_logout'),
    path('accounts/', include('allauth.urls')),
    path('user_order', views.user_order, name='user_order'),
    path('admin_order', views.admin_order, name='admin_order'),
    path('approve_order/<int:id>',views.approve_order,name='approve_order'),
    path('approved_order',views.approved_order,name='approved_order'),
    path('admin_product',views.admin_product,name='admin_product'),

    # path('success', views.success, name = 'success'),



]

urlpatterns =urlpatterns + static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)