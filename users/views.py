from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

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
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        phone = request.POST['phone']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Tên người dùng đã tồn tại.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email đã được sử dụng.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.profile.phone = phone
                user.profile.plain_password = password  # Lưu mật khẩu không mã hóa
                user.profile.save()
                messages.success(request, 'Đăng ký thành công. Bạn có thể đăng nhập.')
                return redirect('login')
        else:
            messages.error(request, 'Mật khẩu không khớp.')
    return render(request, 'register.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'Đăng xuất thành công.')
    return redirect('index')