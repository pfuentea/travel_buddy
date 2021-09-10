from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required


@login_required
def index(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


@login_required
def addtrip(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'addtrip.html', context)



@login_required
def view(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'view.html', context)


@login_required
def detail(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'detail.html', context)
