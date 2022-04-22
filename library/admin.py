from django.contrib import admin

# Register your models here.
from .models import Book, Fichas

admin.site.register(Fichas)
admin.site.register(Book)