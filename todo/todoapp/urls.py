from django.urls import path
from . import views

app_name = "todoapp"
urlpatterns = [
    path("", views.home, name="home"),
    path("add_task", views.add_task, name="add_task"),              
    path("mark_task", views.mark_task, name="mark_task"), 
    path("add_sub_task", views.add_sub_task, name="add_sub_task"),  
    path("delete_task", views.delete_task, name="delete_task"),  
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results", views.results, name="results"),
    # path("<int:question_id>/vote", views.vote, name="vote")
    
]