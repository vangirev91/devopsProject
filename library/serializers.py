from dataclasses import field
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "pk",
            "codigo_ficha",
            "fecha_publicacion",
            "color",
            "descripcion",

        ]
        extra_kwargs = {
            "fecha_publicacion" : {"required":False},
            "color" : {"required":False},
            "descripcion" : {"required":False},
        }