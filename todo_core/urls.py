from django.urls import path
from .views import homepage, todo_list, todo_detail, complete_todo, delete_todo, edit_todo

urlpatterns = [
    path("", homepage, name="home"),
    path("todos", todo_list, name="todos"),
    path("todos/<int:pk>", todo_detail, name="todo"),
    path("todos/<int:pk>/complete", complete_todo, name="mark_complete"),
    path("todos/<int:pk>/delete", delete_todo, name="delete_todo"),
    path("todos/<int:pk>/edit", edit_todo, name="edit_todo"),
]