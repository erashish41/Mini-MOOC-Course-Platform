from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course.views import (
    CourseView
)

router = DefaultRouter()
router.register("courses", CourseView, basename="courses")


urlpatterns = [
    path("", include(router.urls)),
]