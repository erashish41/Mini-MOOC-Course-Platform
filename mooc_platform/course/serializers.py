from rest_framework import serializers
from course.models import Course, Lesson, Enrollment, LessonProgress

class LessonSerializer(serializers.ModelSerializer):
    viewed = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ["id", "title", "content", "created_at", "viewed"]
        
    def get_viewed(self,obj):
        user = self.context["request"].user
        if user.is_anonymous:
            return False
        return LessonProgress.objects.filter(
            user=user, lesson=obj, viewed=True
        ).exists()

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ["id", "title", "short_description", "long_description", "created_at", "lessons"]
        
        
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ["id", "course", "enrolled_at"]