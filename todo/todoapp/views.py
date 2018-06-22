from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .models import Task
import datetime
import json
# Create your views here.

@login_required
def home(request):
    todo_list = Task.objects.filter(user=request.user, is_deleted=False)
    context = {
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
        due_date = request.POST.get("due_date", datetime.date.today)
        task = Task(user= request.user, title=title, due_date=due_date)
        task.save()
        response_dict["status"] = "SUCCESS"
        return json.dumps(response_dict)
    else:
        response_dict["status"] = "FAIL"
        response_dict["error"] = "BAD_METHOD"
    