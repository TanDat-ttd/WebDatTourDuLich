from django.shortcuts import render


def index(request):
    return render(request, 'index.html')  # Hiển thị file index.html


def about(request):
    return render(request, 'about.html')  # Hiển thị file register.htmlfrom django.shortcuts import render

