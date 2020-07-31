from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request, "tasks1/index.html",{
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task=form.cleaned_data["task"]
            request.session["tasks"] += [new_task]
	#redirect to tasks page
            return HttpResponseRedirect(reverse("tasks1:index"))
        else:
	#return the invalid form back
            return render(request, "tasks1/add.html", {
            "form": form
            })
	#return empty form request method is not post
    return render(request, "tasks1/add.html", {
        "form": NewTaskForm()   
    })

