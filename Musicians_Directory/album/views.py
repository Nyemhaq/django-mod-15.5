from django.shortcuts import render,redirect
from . models import Album
from . forms import albumForm
from musician.models import Musician
from musician.forms import musicianForm

def album(req):
    data = Album.objects.all()
    return render(req,'album/album.html',{'data':data})

def edit(req, id):
    album = Album.objects.get(pk = id)
    form = albumForm(instance=album)
    if req.method == 'POST':
        form = albumForm(req.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album')
    return render (req,'album/edit.html',{'form':form})

def edit_name(req, id):
    musician = Musician.objects.get(pk = id)
    form = musicianForm(instance=musician)
    if req.method == 'POST':
        form = musicianForm(req.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('album')
    return render (req,'musician/edit.html',{'form':form})

def delete(req, id):
    album = Album.objects.get(pk = id).delete()
    return redirect('album')
