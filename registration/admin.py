from django.contrib import admin
from .models import Foo,server_loogin
from .models import server_products,city_names,country_name,orders
# Register your models here.
admin.site.register(Foo)
admin.site.register(server_loogin)
admin.site.register(server_products)
admin.site.register(city_names)
admin.site.register(country_name)
admin.site.register(orders)