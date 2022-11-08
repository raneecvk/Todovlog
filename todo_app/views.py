from .forms import Todoforms
from django.shortcuts import render,redirect
from django . http import HttpResponse
from . models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.

class TaskListView(ListView):
    model=Task
    template_name='index.html'
    context_object_name='obj1'
class TaskDetailView(DetailView):
    model=Task
    template_name='details.html'
    context_object_name='i'


def index(request):
    obj1=Task.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        priority = request.POST.get("priority")
        date=request.POST.get("date")
        obj = Task(name=name, priority=priority,date=date)
        obj.save()
    return render(request,'index.html',{'obj1':obj1})



def home(request):

    return render(request,'home.html')

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoforms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})