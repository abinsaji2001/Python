from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from . forms import TodoForm
from django .views .generic import ListView
from django .views .generic.detail import DetailView
from django .views .generic.edit import UpdateView
from django .views .generic.edit import DeleteView


class Tasklistview(ListView):
    model=task
    template_name ='home.html'
    context_object_name ='x'

class Taskdetailview(DetailView):
    model= task
    template_name = 'detail.html'
    context_object_name = 't1'

class Taskupdateview(UpdateView):
    model= task
    template_name = 'update.html'
    context_object_name = 't'
    fields =('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class Taskdeleteview(DeleteView):
    model= task
    template_name = 'delete.html'
    success_url =('cbvhome')










# Create your views here.
def home(request):
    task2 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        priority = request.POST.get('priority')
        date= request.POST.get('date')
        task1=task(name=name,priority=priority,date=date)
        task1.save()
    return render(request,'home.html',{'x':task2})


def delete(request,taskid):
    t1=task.objects.get(id=taskid)
    if request.method == 'POST':
        t1.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    t2=task.objects.get(id=id)
    f=TodoForm(request.POST or None ,instance=t2)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'t=':t2 , 'f':f})
