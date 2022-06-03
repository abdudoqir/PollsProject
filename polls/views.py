from django.shortcuts import render

# Create your views here.
from django.views import generic

from polls.models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')