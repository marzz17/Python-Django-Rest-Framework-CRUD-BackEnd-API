from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import employeeleave_serializer
from .models import Employeeleave


class EmployeeleaveViewSet(viewsets.ModelViewSet):
    queryset = Employeeleave.objects.all()
    serializer_class = employeeleave_serializer