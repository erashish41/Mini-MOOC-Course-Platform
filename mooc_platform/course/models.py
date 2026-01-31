from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="lessons")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("course", "title")
    
    def __str__(self):
        return self.title
    
    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="enrollments")
    enrolled_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("user", "course")
    
    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
    
    
class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name="progress")
    viewed = models.BooleanField(default=False)
    viewed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"