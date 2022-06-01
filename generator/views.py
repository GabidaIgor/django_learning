from django.shortcuts import render
from django.http import HttpResponse
import string
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def new_password(request):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    length = int(request.GET.get('length', 10))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    special = request.GET.get('special')

    all_characters = lower

    if uppercase == 'on':
        all_characters += upper

    if numbers == 'on':
        all_characters += num

    if special == 'on':
        all_characters += symbols

    temp_password = random.sample(all_characters, length)

    generated_password = ''.join(temp_password)

    return render(request, 'generator/new_password.html', {'password': generated_password})
