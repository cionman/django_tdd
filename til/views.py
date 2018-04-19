from datetime import date

from django.shortcuts import render, redirect

from til.forms import TilForm
from til.models import Til


def til(request):
    if request.method == 'POST':
        form = TilForm(request.POST)
        if form.is_valid():
            til = Til(**form.cleaned_data)
            til.save()
            return redirect('til:til')
    else:
        form = TilForm()
    return render(request, 'til/til.html', {
        'form': form
        , 'now': date.today()
        , 'til_list': Til.objects.all()
    })
