from django.shortcuts import render

def add_address(request):
    return render(request, 'address_book/add_address.html', {})

