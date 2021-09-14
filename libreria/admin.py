from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Libros)
class LibrosAdmin(admin.ModelAdmin):
    list_display = ("id","titulo","descripcion","isbn","autor")