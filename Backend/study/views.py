from django.http import JsonResponse
from .models import Progress

def get_progress(request):

    progress_data = Progress.objects.all()

    data = []

    for p in progress_data:
        data.append({
            "user": p.user.username,
            "subject": p.subject,
            "quizzes_taken": p.quizzes_taken,
            "average_score": p.average_score
        })

    return JsonResponse(data, safe=False)
