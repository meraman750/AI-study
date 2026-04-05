from django.urls import path
from .views import GenerateSummary, GenerateQuiz, AITest

urlpatterns = [
    path("ai/test/", AITest.as_view()),

    path("ai/summary/<int:material_id>/", GenerateSummary.as_view()),
    path("ai/quiz/<int:material_id>/", GenerateQuiz.as_view()),
]