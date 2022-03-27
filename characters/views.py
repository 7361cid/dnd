from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Character


class Homepage(TemplateView):
    template_name = 'home.html'


class CharactersListView(ListView):
    model = Character
    template_name = 'characters.html'


class CharactersDetailView(DetailView):
    model = Character
    template_name = 'character_detail.html'


class CharactersCreateView(CreateView):
    model = Character
    template_name = 'character_new.html'
    fields = '__all__'