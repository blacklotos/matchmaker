from django.contrib.auth.models import User
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect
from .models import Question, Answer, UserAnswer
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib import messages

#Mandatory == 300
#Very Important == 100
#Somewhat Important == 20
#Not Important == 0

def all_questions(request):
    questions_all = Question.objects.all()
    paginator = Paginator(questions_all, 5)
    importance_levels = ['Mandatory', 'Very Important', 'Somewhat Important', 'Not Important']

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    if request.method == "POST":
        importance_levels = request.POST['importance_levels']
        question_id = request.POST['question_id']
        answer_form =  request.POST['answer']
        user = User.objects.get(username=request.user)
        question = Question.objects.get(id=question_id)
        answer = Answer.objects.get(question=question, answer=answer_form)
        answered, created = UserAnswer.objects.get_or_create(user=user, question=question)
        answered.answer = answer
        answered.importance_levels = importance_levels
        answered.save()
        messages.success(request, 'Answer saved.')
    return render_to_response('questions/all.html', locals(), context_instance=RequestContext(request))