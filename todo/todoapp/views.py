from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .models import Task, SubTask
import datetime
from dateutil import parser as date_parser
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required
def home(request):
    filter_type = request.GET.get("filter", "")
    if filter_type == "today":
        todo_list = Task.objects.filter(user=request.user, is_deleted=False, due_date=datetime.date.today())
    elif filter_type == "this_week":
        a = 1
    elif filter_type == "next_week":
        a = d
    elif filter_type == "overdue":
        todo_list = Task.objects.filter(user=request.user, is_deleted=False, is_completed=False)
    else:
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
def mark_task(request):
    response_dict = {}
    if request.method == "POST":
        task_id = request.POST.get("id","")
        task = Task.objects.filter(id=task_id, user=request.user, is_deleted=False).first()
        if task is None :
            response_dict["status"] = "FAIL"
            response_dict["error"] = "TASK_DOES_NOT_EXIST"
        else:
            is_completed = request.POST.get("is_completed","FALSE")
            # print(type(is_completed)) --> always str
            # print(is_completed) 
            if is_completed=="TRUE" and not task.is_completed:
                task.is_completed = True
            else:
                task.is_completed = False
            task.save()
            response_dict["status"] = "OK"
    else:
        response_dict["status"] = "FAIL"
        response_dict["error"] = "BAD_METHOD"
    return HttpResponse(json.dumps(response_dict))



@login_required
def add_sub_task(request):
    response_dict = {}
    if request.method == "POST":
        task_id = request.POST.get("task_id", "")
        user = request.user
        task = Task.objects.filter(id=task_id, user=request.user, is_deleted=False).first()
        if task is None :
            response_dict["status"] = "FAIL"
            response_dict["error"] = "TASK_DOES_NOT_EXIST"
        else:
            if request.POST.get("multiple", "TRUE") == "TRUE" :
                sub_tasks = request.POST.get("sub_tasks", "")
                for each in json.loads(sub_tasks):
                    # print(each)
                    # print(type(each))
                    sub_task = SubTask(task= task, title= each["title"])
                    sub_task.save()
                response_dict["status"] = "OK"
            else:
                sub_task = request.POST.get("sub_task", "")
                sub_task_obj = SubTask(task= task, title= sub_task["title"])
                sub_task_obj.save()
                response_dict["status"] = "OK"
    else:
        response_dict["status"] = "FAIL"
        response_dict["error"] = "BAD_METHOD"
    return HttpResponse(json.dumps(response_dict))
            



    