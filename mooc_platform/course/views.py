from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now


from django.shortcuts import render
from course.models import Course, Lesson, Enrollment, LessonProgress

from course.serializers import (
    CourseSerializer
)
# Create your views here.


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    
@action(detail=True, methods=["post"])
def enroll_course(self,request,pk=None):
    course = self.get_object()
    Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )
    return Response({"message":"Enrolled"})
    
    
class LessonProgressViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        LessonProgress.objects.update_or_create(
            user=request.user,
            lesson_id=request.data.get("lesson"),
            defaults={
                "viewed": True,
                "viewed_at": now(),
            },
        )
        return Response({"status": "Lesson marked as viewed"})