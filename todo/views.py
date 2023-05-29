
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Branch, Todo
from . import forms

# Create your views here.

class HomeView(generic.ListView):
    model = Branch
    template_name = 'branch_list.html'


def addBranch(request):

    if request.method == "POST":

        form = forms.BranchForm(request.POST)

        if form.is_valid():

            branch = form.save()

            return redirect('todo:branch',branch.id)

    else:
        form = forms.BranchForm()

    context = {'form':form}
    return render(request, 'addBranch.html', context)


def updateBranch(request, branch_name):
    
    branch = get_object_or_404(Branch, name = branch_name)
    

    form = forms.BranchForm(request.POST or None, instance=branch)


    if form.is_valid():

        form.save()
        return redirect('todo:branch',branch.id)
    

    context = {'form':form}
    return render(request, 'updateBranch.html', context)
   

def deleteBranch(request, branch_name):
    branch = get_object_or_404(Branch, name = branch_name)
    branch.delete()
    return redirect('todo:home')



class BranchDetail(generic.DetailView):
    model = Branch
    template_name = 'todo_list.html'
    context_object_name = 'branch'

    def get_context_data(self, **kwargs):
        context = super(BranchDetail,self).get_context_data(**kwargs)
        context['object_list'] = Todo.objects.filter(branch=self.get_object())
        return context



def addToDo(request, branch_name):

    if request.method == "POST":

        form = forms.ToDoForm(request.POST)

        if form.is_valid():

            todo = form.save(commit=False)
            todo.branch= Branch.objects.get(name = branch_name)
            todo.save()

            return redirect('todo:branch',todo.branch.id) 
    else:
        form = forms.ToDoForm()

    context = {'form':form}
    return render(request, 'addToDo.html', context)


def addFullToDo(request):

    if request.method == "POST":

        form = forms.FullToDoForm(request.POST)

        if form.is_valid():

            todo = form.save()

            return redirect('todo:branch',todo.branch.id)
        
    else:
        form = forms.FullToDoForm()

    context = {'form':form}
    return render(request, 'addToDo.html', context)


def updateToDo(request, todo_title):
    
    todo = get_object_or_404(Todo, title = todo_title)
    

    form = forms.FullToDoForm(request.POST or None, instance=todo)


    if form.is_valid():

        form.save()
        return redirect('todo:branch',todo.branch.id)   
    

    context = {'form':form}
    return render(request, 'updateToDo.html', context)
   

def deleteToDo(request, todo_title):
    todo = get_object_or_404(Todo, title = todo_title)
    todo.delete()
    return redirect('todo:branch',todo.branch.id)    ###########################


def thanks(request):
    return render(request, 'thanks.html')


class ToDoDetailView(generic.DetailView):

    model = Todo
    template_name = 'todoDetail.html'


def finishToDo(request, todo_id):

    todo = get_object_or_404(Todo, pk=todo_id)
    todo.activity = 'P'
    todo.save()
    branch = todo.branch
    return redirect('todo:branch',todo.branch.id)    ###########################



class HandledToDoView(generic.ListView):

    model = Todo
    queryset = Todo.objects.filter(activity='P')
    template_name = 'handledToDo_list.html'


class SoonComeToDoView(generic.ListView):

    model = Todo
    template_name = 'soonComeToDo_list.html'

class AllToDoView(generic.ListView):

    model = Todo
    template_name = 'allToDos.html'
