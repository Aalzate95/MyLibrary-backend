from django.db.models import Model, CASCADE, DO_NOTHING, SET_NULL
from django.db.models import ForeignKey, OneToOneField, ManyToManyField
from django.db.models import (
    CharField,
    IntegerField,
    FloatField,
    DateTimeField,
    TimeField,
    BooleanField,
    FileField,
    UUIDField,
    DateField
)
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
# Create your models here.



class Autores(Model):
    nombre = CharField(max_length=200, blank=False)
    apellido = CharField(max_length=200, blank=False)
    nacionalidad = CharField(max_length=100, blank=True, null=True)
    created_date = DateTimeField(auto_now_add=True, null=True, db_index=True)
    updated_date = DateTimeField(auto_now=True)
    

class Libros(Model):
    titulo = CharField(max_length=200, blank=False)
    descripcion = CharField(max_length=500, blank=True)
    isbn = CharField(max_length=10, blank=True)
    imagen = CharField(max_length=500, blank=True)
    autor = CharField(max_length=200, blank=True)
    created_date = DateTimeField(auto_now_add=True, null=True, db_index=True)
    updated_date = DateTimeField(auto_now=True)


