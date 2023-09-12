from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
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
   


def pokemons_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemons/detail.html', {
        'pokemon': pokemon
    })
class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['description']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemons'
