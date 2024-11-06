from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from coursesApp.models import Course
from coursesApp.serializers import CourseSerializer


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


