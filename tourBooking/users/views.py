
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Đăng nhập thành công!')
            return redirect('index')  # Chuyển hướng đến trang chủ sau khi đăng nhập thành công
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Tên người dùng đã tồn tại.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email đã được sử dụng.')
            else:
                try:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.success(request, 'Đăng ký thành công. Bạn có thể đăng nhập.')
                    return redirect('login')
                except IntegrityError:
                    messages.error(request, 'Có lỗi xảy ra. Vui lòng thử lại.')
        else:
            messages.error(request, 'Mật khẩu không khớp.')
    return render(request, 'register.html')

def logout(request):
    auth_logout(request)
    return redirect('index')