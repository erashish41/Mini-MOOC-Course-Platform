from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course.views import (
    CourseViewSet, LessonProgressViewSet
)

router = DefaultRouter()
router.register("courses", CourseViewSet, basename="courses")
router.register("my-courses", LessonProgressViewSet, basename="my-courses")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "lesson-progress/",
        LessonProgressViewSet.as_view({"post": "create"}),
    ),
]