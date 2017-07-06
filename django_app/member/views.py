from django.contrib.auth import authenticate, logout as django_logout, login as django_login
from django.http import HttpResponse
from django.shortcuts import redirect, render


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            django_login(request, user)
            return redirect('post:post_list')
        else:
            return HttpResponse('Login credentials invalid')


    else:
        if request.user.is_authenticated:
            return redirect('post:post_list')
        return render(request, 'member/login.html')


def logout(request):
    django_logout(request)
