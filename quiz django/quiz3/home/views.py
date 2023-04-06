from django.shortcuts import render
from .models import *
import random

def home(request):
    context = {'categories' : Category.objects.all()}
    return render(request ,'home.html' , context)


def get_quiz (request):
    try:
            question_objs = Question.objects.all()
            data = []
            random.shuffle(list(question_objs))

            print(question_objs)

            for question_obj in question_objs:
                 data.append({
                      "category" : question_obj.category.category_name,
                      "question" : question_obj.question,
                      "marks" : question_obj.marks,
                      "answers" : question_obj.get_answers()
                      })
            payload = {'status' : True}

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong")