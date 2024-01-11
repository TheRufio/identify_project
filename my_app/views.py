from django.shortcuts import render, redirect
from .models import MyUsers, Blogs
from django.contrib import messages

def home(request):
    users = MyUsers.objects.all()
    blogs = Blogs.objects.all()
    return render(request, 'my_app/home.html', {'users' : users,
                                                'blogs' : blogs})

def registration(request):
    if request.method == 'GET':
            return render(request, 'my_app/registration.html')
    
    elif request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if nickname and password and email:
            if len(nickname) > 60:
                messages.error(request, 'Занадто довгий логін! Максимум 60 символів')

            elif '@' not in email and '.' not in email:
                messages.error(request, 'Формат пошти введено не правильно!')
            else:
                return redirect('/main/')
        return render(request, 'my_app/registration.html', {'nickname' : nickname,
                                                            'password' : password,
                                                            'email' : email})


