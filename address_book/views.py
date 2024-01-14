from django.shortcuts import render
from .models import Address

def add_address(request):
    all_addresses = Address.objects.all()
    return render(request, 'address_book/add_address.html', {'all_addresses': all_addresses})

def my_address_book(request):
    all_addresses = Address.objects.all()
    return render(request, 'address_book/my_address_book.html', {'all_addresses': all_addresses})

def my_view(request):
    number_of_records = Address.objects.count()
    return render(request, 'address_book/my_template.html', {'number_of_records': number_of_records})

def addresses(request):
    addresses = Address.objects.all()
    return render(request, 'address_book/address_list.html', {'addresses': addresses})

def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'address_book/address_list.html', {'addresses': addresses})
