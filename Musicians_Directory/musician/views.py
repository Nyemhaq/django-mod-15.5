from django.shortcuts import render
from .models import Musician
from .forms import musicianForm

def edit_musician(req,id):
    musician = Musician.objects.get(pk = id)
    form = musicianForm(instance=musician)
    if req.method == 'POST':
        form = musicianForm(req.POST)
        if form.is_valid():
            form.save()
            
    return render (req,'musician/edit.html',{'form':form})