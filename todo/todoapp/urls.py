from django.urls import path
from . import views

app_name = "todoapp"
urlpatterns = [
    path("", views.home, name="home"),
    path("add_task", views.add_task, name="add_task"),
    path("mark_completed", views.mark_task_completed, name="mark_completed"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results", views.results, name="results"),
    # path("<int:question_id>/vote", views.vote, name="vote")
    
]