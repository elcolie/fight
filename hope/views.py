from django.core.urlresolvers import reverse_lazy
from fight.models import Hope
from fight.forms import HopeForm
from vanilla import CreateView, DeleteView, ListView, UpdateView


class ListNotes(ListView):
    model = Note


class CreateNote(CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('list_notes')


class EditNote(UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('list_notes')


class DeleteNote(DeleteView):
    model = Note
    success_url = reverse_lazy('list_notes')
