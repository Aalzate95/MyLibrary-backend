from rest_framework.serializers import ModelSerializer

from . import models


class LibrosSerializer(ModelSerializer):
    class Meta:
        model = models.Libros
        fields = ["id","titulo","descripcion","isbn","imagen","autor"]