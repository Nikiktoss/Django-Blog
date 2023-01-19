from django.shortcuts import render, redirect
from .forms import *
from .models import Action


def index(request):
    last_actions = Action.objects.order_by("-date_create")[:10]
    number_of_all_notes = len(Note.objects.all())
    notes = Note.objects.order_by("-date_create")[:3]
    return render(request, 'blog_templates/index.html', context={'notes': notes, 'number': number_of_all_notes,
                                                                 'actions': last_actions})


def view_all_notes(request):
    notes = Note.objects.all()
    return render(request, 'blog_templates/view_all_notes.html', context={'notes': notes})


def note_view(request, slug):
    note = Note.objects.get(slug=slug)
    return render(request, 'blog_templates/note.html', context={'note': note})


def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = Note.objects.create(**form.cleaned_data)
            title = f"Создание записи '{note.title}'"
            action = Action.objects.create()
            action.action = title
            action.save()
            return redirect('main_page')
    else:
        form = NoteForm()
    return render(request, 'blog_templates/add_note.html', context={'form': form})


def update_note(request, slug):
    note = Note.objects.get(slug=slug)
    if request.method == "POST":
        form = NoteUpDateForm(request.POST, instance=note)
        if form.is_valid():
            note.title = form.cleaned_data['title']
            note.content = form.cleaned_data['content']
            note.slug = form.cleaned_data['slug']
            act = Action()
            act.action = f"Редактирование записи '{note.title}'"
            act.save()
            note.save()
            return redirect('main_page')
    else:
        form = NoteUpDateForm(instance=note)
    return render(request, 'blog_templates/update_note.html', context={'id': note.id, 'form': form, 'slug': note.slug})


def delete_note(request, slug):
    note = Note.objects.get(slug=slug)
    if request.method == "POST":
        act = Action()
        act.action = f"Удаление записи '{note.title}'"
        act.save()
        note.delete()
        return redirect('main_page')
    return render(request, 'blog_templates/delete_note.html', context={'note': note})


def delete_some_notes(request):
    notes = Note.objects.all()
    if request.method == "POST":
        list_of_delete_ids = request.POST.getlist('choices')
        for note_id in list_of_delete_ids:
            note = Note.objects.get(id=int(note_id))
            note.delete()

        if len(list_of_delete_ids) != 0:
            act = Action()
            act.action = "Удаление нескольких записей сразу"
            act.save()
        return redirect('main_page')
    return render(request, 'blog_templates/delete_some_notes.html', context={'notes': notes})


def search_for_note(request):
    title = str(request.POST['note_title'])
    all_notes = Note.objects.all()
    notes = []

    for note in all_notes:
        if note.is_search_result(title):
            notes.append(note)

    return render(request, 'blog_templates/search_for_note.html', context={'notes': notes})
