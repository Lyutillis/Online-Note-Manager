from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os
from .models import Note

# Create your views here.
def home_page_view(request) :
    context={'notes': []}
    user=request.user
    if user.is_authenticated :
        notes = Note.objects.filter(user=user.id)
        context['notes']=list(notes)
    return render(request, 'index.html', context)

def create_note_view(request) :
    user=request.user
    if request.method == 'POST' :
        title = request.POST.get('title')
        body = request.POST.get('body')
        if user.is_authenticated :
            note = Note.create(title, body, user.id)
            if note != None :
                messages.success(request, ("Заметка успешно добавлена!"))
                return redirect('home')
        else :
            messages.success(request, ("Пользователь не зарегистрирован!"))
            return render(request, 'create_note.html', {'title': title,'body': body,})
    return render(request, 'create_note.html', {})

def edit_note_view(request, id) :
    note = Note.get_by_id(id)
    context={'title': note.title,
    'body': note.body,
    }
    if request.method=='POST' :
        title = request.POST.get('title')
        body = request.POST.get('body')
        note.update(title, body)
        messages.success(request, ("Заметка успешно отредактирована!"))
        return redirect('/')
    return render(request, 'edit_note.html', context)

def searchbar_view(request) :
    user=request.user
    context={
        'notes': [],
        }
    if request.method == 'GET' :
        list_to_process = Note.objects.filter(user=user.id)
        query = request.GET.get('query')
        if query and list_to_process : 
            for i in list_to_process :
                if query in i.title or query in  i.body :
                    context['notes'].append(i)
            messages.success(request, ("Поиск окончен успешно!"))
        else : 
            render(request, 'searchbar.html', context)
    return render(request, 'searchbar.html', context)

def delete_note_view(request, id) :
    note = Note.objects.get(pk=id)
    note.delete()
    return redirect('/')