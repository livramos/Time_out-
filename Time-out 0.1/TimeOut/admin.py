from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import usuario

# Register your models here.

class usuarioAdmin (admin.ModelAdmin):
  list_display = ['nome','email','senha']

admin.site.register(usuario, usuarioAdmin)