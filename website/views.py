from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html', {})


def vision(request):
    return render(request, 'website/vision.html', {})