from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .models import Task
import datetime
from dateutil import parser as date_parser
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required
def home(request):
    todo_list = Task.objects.filter(user=request.user, is_deleted=False)
    context = {
        'title': 'Todo-App',
        'todo_list': todo_list
    }
    # my_template = loader.get_template("polls/home.html")
    # return HttpResponse(my_template.render(context, request))
    return render(request, "todoapp/home.html", context)

@login_required
def add_task(request):
    response_dict = {}
    if request.method == "POST":
        title = request.POST.get("title","NO_TITLE")
        due_date = request.POST.get("due_date", str(datetime.date.today()))
        # due_date = date_parser.parse(due_date) 
        due_date = due_date.split("GMT")[0]
        due_date = datetime.datetime.strptime(due_date.strip(), "%a %b %d %Y %H:%M:%S")
        #print(type(due_date))
        task = Task(user= request.user, title=title, due_date=due_date)
        task.save()
        response_dict["status"] = "OK"
        return HttpResponse(json.dumps(response_dict))
    else:
        response_dict["status"] = "FAIL"
        response_dict["error"] = "BAD_METHOD"
        return HttpResponse(json.dumps(response_dict))


@login_required
def show_task(request):
    return HttpResponse("Hi")


@login_required
def mark_task_completed(request):
    response_dict = {}
    if request.method == "POST":
        task_id = request.POST.get("id","")
        task = Task.objects.filter(id=task_id, user=request.user, is_deleted=False).first()
        if task is None :
            response_dict["status"] = "FAIL"
            response_dict["error"] = "TASK_DOES_NOT_EXIST"
        else:
            if task.is_completed == False:
                task.is_completed = True
                task.save()
            response_dict["status"] = "OK"
    else:
        response_dict["status"] = "FAIL"
        response_dict["error"] = "BAD_METHOD"
    return HttpResponse(json.dumps(response_dict))


            



    