from django.urls import path
from .views import GenerateSummary, GenerateQuiz, AITest

urlpatterns = [
    path("test/", AITest.as_view()),

    path("summary/<int:material_id>/", GenerateSummary.as_view()),
    path("quiz/<int:material_id>/", GenerateQuiz.as_view()),
]