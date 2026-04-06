from rest_framework.views import APIView
from rest_framework.response import Response
from .ai.ai_service import AIService
from .models import StudyMaterial, Summary
import json
from .models import Quiz, Question
# from .ai.utils import chunk_text


from rest_framework.views import APIView
from rest_framework.response import Response
from .ai.ai_service import AIService


class AITest(APIView):

    def post(self, request):

        text = request.data.get("text")

        if not text:
            return Response({"error": "Provide text"}, status=400)

        summary = AIService.generate_summary(text)
        quiz = AIService.generate_quiz(text)

        return Response({
            "summary": summary,
            "quiz": quiz
        })

class GenerateQuiz(APIView):

    def post(self, request, material_id):

        material = StudyMaterial.objects.get(id=material_id)

        quiz_data = AIService.generate_quiz(material.content)

        quiz_json = json.loads(quiz_data)

        quiz = Quiz.objects.create(material=material)

        for q in quiz_json:
            Question.objects.create(
                quiz=quiz,
                question_text=q["question"],
                options=q["options"],
                correct_answer=q["answer"],
            )

        return Response({"message": "Quiz created"})


class GenerateSummary(APIView):

    def post(self, request, material_id):
        material = StudyMaterial.objects.get(id=material_id)

        summary_text = AIService.generate_summary(material.content)

        Summary.objects.create(
            material=material,
            content=summary_text
        )

        return Response({"summary": summary_text})


# class ChatBot(APIView):

#     def post(self, request, material_id):

#         question = request.data["question"]
#         material = StudyMaterial.objects.get(id=material_id)

#         chunks = chunk_text(material.content)

#         context = chunks[0]  # simple version

#         answer = AIService.chat(question, context)

#         return Response({"answer": answer})