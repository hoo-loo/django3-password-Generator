from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def help(request):
    return render(request, "Password_Generator.html")

def generate(request):
    password = ''
    charlist = 'abcdefghijklmnopqrstuvwxyz'
    length = int (request.GET.get("length"))

    if request.GET.get('Uppercase') == 'on':
        charlist += charlist.upper()
        charlist = list(charlist)

    if request.GET.get('Numbers') == 'on':
        charlist += list('0123456789')

    for i in range(length):
        password += random.choice(charlist)

    return render(request,'Generated.html', {"generated_pass":password})

def about(request):
    return render(request, "AboutMyself.html")