from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon


# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

class PokemonList(ListView):
    model = Pokemon
    template_name = 'pokemons/index.html'
    context_object_name = 'pokemons'
   
class PokemonDetail(DetailView):
    model = Pokemon
    template_name = 'pokemons/detail.html'
    context_object_name = 'pokemon'

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['description']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemons'
