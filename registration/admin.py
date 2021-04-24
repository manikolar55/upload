from django.contrib import admin
from .models import Foo,server_loogin
from .models import server_products
# Register your models here.
admin.site.register(Foo)
admin.site.register(server_loogin)
admin.site.register(server_products)