from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from .models import Question


#def index(request):
#    return HttpResponse(" ¡¡Hola mundo!! ")

# Create your views here.
#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('miapp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'miapp/index.html', context)



# ...
def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'miapp/detail.html', {'question': question})

