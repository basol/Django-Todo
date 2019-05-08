from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Todo
from .forms import CreateTodoModelForm
from .admin import TodoResource
from import_export import resources
import tablib
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home_page(request):
    objects = Todo.objects.all()
    template_name = "home.html"
    context = { "objects": objects}
    return render(request, template_name, context)

@login_required
def update(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('/')

@login_required
def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('/')
    
@login_required
def create_todo(request):
    form = CreateTodoModelForm(request.POST or None)
    if request.method == 'POST':   
        if form.is_valid():
            print(form.cleaned_data)
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form = CreateTodoModelForm()
            return redirect('/')
        else: print("errror")
    context = {"form": form}

    template_name = "create-todo.html"
    return render(request, template_name, context)

@login_required
def import_todo(request):
    todo_resource = resources.modelresource_factory(model=Todo)()
    dataset = tablib.Dataset(['id', 'New Todo'], headers=['text', 'is_completed'])
    result = todo_resource.import_data(dataset, dry_run=True)
    print(result.has_errors())
    result = todo_resource.import_data(dataset, dry_run=False)
    return redirect('/')

@login_required
def export_todo(request):
    dataset = TodoResource().export()
    print(dataset.csv)
    f = open("exported-todo-list.csv","w+")
    f.write(str(dataset.csv))
    f.close()
    return redirect('/')

@login_required
def user_profile(request, id):

    return render(request, 'user_profile.html')


def statistics_page(request):

    data = Todo.objects.values_list('is_completed', flat=True)
    print(data)
    context = {"data": [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6]]}
    template_name='statistics.html'
    return render( template_name, context)