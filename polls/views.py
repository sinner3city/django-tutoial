from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.utils import timezone

from .models import Choice, Question


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



#old code urls

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def pyt(request, question_text):
#     print(question_text)
#     question = get_object_or_404(Question, pk=question_text)
#     return render(request, 'polls/pyt.html', {'question': question})



# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #3
        test_post = request.POST.get('choice_text')
        print(test_post)
        print(selected_choice)
        print(question_id)
        
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.choice_text = test_post
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


    
def choices(request):
    choices = Choice.objects.all()
    context = {
        'title': 'Wszystkie odpowiedzi',
        'choices': choices,
    }
    return render(request, 'polls/choices.html', context)