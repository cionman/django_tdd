from django.shortcuts import render, redirect

from toy.forms import ToyForm
from toy.models import Toy


def create_toy(request):
    if request.method == 'POST':
        form = ToyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('toy:toy')
    else:
        form=ToyForm()
    return render(request,'toy/toy.html',{
        'form': form
    })
    return None
