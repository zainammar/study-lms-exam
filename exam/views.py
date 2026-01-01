from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Option, UserAnswer, Result

# --- Quiz List ---
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'exam/quiz_list.html', {'quizzes': quizzes})

# --- Quiz Detail ---
@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'exam/quiz_detail.html', {'quiz': quiz})

# --- Submit Quiz ---
@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    score = 0
    total = quiz.questions.count()

    if request.method == 'POST':
        for question in quiz.questions.all():
            selected_option_id = request.POST.get(str(question.id))
            if selected_option_id:
                option = Option.objects.get(id=selected_option_id)
                UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    selected_option=option
                )
                if option.is_correct:
                    score += 1

        Result.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total=total
        )

    return render(request, 'exam/result.html', {
        'quiz': quiz,
        'score': score,
        'total': total
    })
