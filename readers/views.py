import random

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.core.exceptions import ObjectDoesNotExist


def register_reader(request):
    page = 'register'
    context = {
        'page': page,
        'form': UserCreationForm()
    }
    if request.method == "GET":
        return render(request, 'readers/login_register.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('account')
            except IntegrityError:
                return render(request, 'readers/login_register.html', context,
                                  {'error': 'Такое имя уже существует'})

        else:
            return render(request, 'readers/login_register.html', context,
            {'error': 'Пароли не совпадают'})
    # if request.method == "GET":
    #     return render(request, 'readers/login_register.html', {'form': UserCreationForm()})
    # else:
    #     if request.POST['password1'] == request.POST['password2']:
    #         try:
    #             user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
    #             user.save()
    #             login(request, user)
    #             return redirect('profile')
    #         except IntegrityError:
    #             return render(request, 'readers/login_register.html', {'form': UserCreationForm()},
    #                               {'error': 'Такое имя уже существует'})
    #
    #     else:
    #         return render(request, 'readers/login_ register.html', {'form': UserCreationForm()},
    #         {'error': 'Пароли не совпадают'})


def login_reader(request):
    if request.method == 'GET':
        return render(request, 'readers/login_register.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'readers/login_register.html', {'form': AuthenticationForm(), 'error': "Неверные данные для входа"})
        else:
            login(request, user)
            return redirect("index")

def logout_reader(request):
    logout(request)
    return redirect('index')


def profile(request, pk):
    prof = Profile.objects.get(id=pk)
    img_list = ['readers/default.png', 'readers/default1.png', 'readers/default2.png']
    rand_img = img_list[random.randint(0, len(img_list) - 1)]
    if prof.profile_image in img_list:
        prof.profile_image = rand_img

    return render(request, 'readers/profile.html', {'profile': prof})

def account(request):
    prof = request.user.profile
    img_list = ['readers/default.png', 'readers/default1.png', 'readers/default2.png']
    rand_img = img_list[random.randint(0, len(img_list) - 1)]
    if prof.profile_image in img_list:
        prof.profile_image = rand_img
    return render(request, 'readers/account.html', {'profile': prof})


@login_required(login_url='login')
def edit_account(request):
    prof = request.user.profile
    form = ProfileForm(instance=prof)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=prof)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'readers/profile_form.html', context)

