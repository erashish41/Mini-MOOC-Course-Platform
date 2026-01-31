from django.contrib import admin
from course.models import Course, Lesson, Enrollment, LessonProgress

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    search_fields = ["title",]
    list_filter = ["created_at"]
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "course", "created_at"]
    search_fields = ["title", "course__title"]
    list_filter = ["course"]
    
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["user", "course", "enrolled_at"]
    search_fields = ["user__username", "course__title"]
    list_filter = ["course"]
    
@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ["user", "lesson", "viewed", "viewed_at"]
    search_fields = ["user__username", "lesson__title"]
    list_filter = ["lesson"]