from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic

from .forms import RegistrationForm, LoginForm, EditUserForm

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('miniblog:index')
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль.')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('miniblog:index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return render(request, 'registration/logout.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('miniblog:profile')
    else:
        form = EditUserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('miniblog:index')
    return render(request, 'delete_profile.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

from django.views import generic

class IndexView(generic.ListView):
    template_name = 'blog/index.html'  # Измените на правильный путь к вашему шаблону
    context_object_name = 'posts'  # Имя контекста, который будет использоваться в шаблоне

    def get_queryset(self):
        # Возвращаем пустой список или фиксированные данные
        return []