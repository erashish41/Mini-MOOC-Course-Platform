from django.shortcuts import render
from course.models import Course, Lesson, Enrollment, LessonProgress
from rest_framework import viewsets, permissions
from course.serializers import (
    CourseSerializer
)
# Create your views here.


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    
    