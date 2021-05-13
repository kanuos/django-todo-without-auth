from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import NoteForm, Note


def homepage(request):
    if request.method == "POST":
        data = NoteForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect("todos")
    context = {
        "form": NoteForm()
    }
    return render(request, "todo_core/home.html", context=context)


def todo_list(request):
    todos = Note.objects.all() or []
    return render(request, "todo_core/todo_list.html", context={"todos": todos})


def todo_detail(request, pk):
    todo = get_object_or_404(klass=Note, pk=int(pk))
    todo.priority = ["Low", "Medium", "High"][int(todo.priority)]
    return render(request, "todo_core/todo_detail.html", context={"todo": todo})


def complete_todo(request, pk):
    todo = get_object_or_404(klass=Note, pk=int(pk))
    todo.complete = not todo.complete
    todo.save()
    return redirect("todos")


def delete_todo(request, pk):
    todo = get_object_or_404(klass=Note, pk=int(pk))
    todo.delete()
    return redirect("todos")


def edit_todo(request, pk):
    todo = Note.objects.get(pk=int(pk))
    print(request.method)
    if request.method == "POST":
        form = request.POST
        todo.title = form["title"]
        todo.detail = form["detail"]
        todo.priority = form["priority"]
        todo.save()
        return redirect("todo", pk)
    else:
        form = NoteForm(instance=todo)
        return render(request, "todo_core/home.html", context={"edit_form": form, "pk": pk})
