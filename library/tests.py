import json
from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from .models import Book
from .serializers import BookSerializer

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data ={
            "codigo_ficha": "pruebaTest",
            "fecha_publicacion": "2022-04-21",
            "color": "naranja",
            "descripcion": "pruebaTest"
            }
        #token = Token.objects.filter(user__username='administrador')
        self.user = User.objects.create_user(username='vane',password='vane123')
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post("/books/", data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()
    def test_registration_some_data(self):
        data ={
            "codigo_ficha": "someData",
            }
        #token = Token.objects.filter(user__username='administrador')
        self.user = User.objects.create_user(username='vane',password='vane123')
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post("/books/", data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()
    def test_get(self):
        response = self.client.get("/books/", format="multipart")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

          