from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

class StudyMaterial(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  # Owner of the material
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)  # Related subject
    title = models.CharField(max_length=255)  # Material title
    file = models.FileField(upload_to="materials/")  # Uploaded file (PDF/DOC)
    extracted_text = models.TextField(blank=True)  # Text extracted for AI processing
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Upload timestamp

class Summary(models.Model):
    material = models.OneToOneField(
        StudyMaterial,
        on_delete=models.CASCADE
    )  # One summary per material

    content = models.TextField()  # AI summary text
    created_at = models.DateTimeField(auto_now_add=True)  # Generation time

class Quiz(models.Model):
    material = models.ForeignKey(
        StudyMaterial,
        on_delete=models.CASCADE
    )  # Quiz based on material

    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    question_text = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_answer = models.CharField(max_length=1)

# Quiz → Many Questions

class QuizAttempt(models.Model):
    # Used For
        # Progress dashboard
        # Statistics
        # Average score
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    score = models.IntegerField()
    total_questions = models.IntegerField()

    attempted_at = models.DateTimeField(auto_now_add=True)


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    quizzes_taken = models.IntegerField(default=0)
    average_score = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.subject}"
