from django.shortcuts import render
from .models import Book

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer

# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer