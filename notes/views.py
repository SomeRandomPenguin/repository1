from django.shortcuts import render, get_object_or_404, redirect
from notes.models import Note
from .forms import NoteForm
# from .models import Note
# from .forms import NoteForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_required
# from django.db.models import queue


def note_list(request):
    notelist = Note.objects.all().order_by('-date_posted')
    return render(request, 'note/note_list.html',  {'note':notelist})

def note_detail(request, note_id): 
    noteid = get_object_or_404(Note, pk=note_id)
    return render(request, 'note/note_detail.html',{'note':noteid})

def create_note(request): 
    if request.method =="POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            # note.author = request.user
            note.save()
            return redirect('note:note_list')
    else:
        form = NoteForm()
    return render(request, 'note/create_note.html', {'form':form})

def about(request):
    return render(request, 'note/about.html')

# Create your views here.