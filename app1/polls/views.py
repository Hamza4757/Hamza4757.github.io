from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    responce = "You are looking at results of question %s ."
    return HttpResponse(responce % question_id)
