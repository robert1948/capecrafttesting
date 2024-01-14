from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html', {})

def vision(request):
    return render(request, 'website/vision.html', {})

def note(request):
    return render(request, 'website/note.html', {}),

def all_addresses(request):
    return render(request, 'website/all_addresses.html', {all_addresses: all_addresses})