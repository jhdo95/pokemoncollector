from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon
from .forms import BerriesForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['berries_form'] = BerriesForm()
        return context

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['description']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemons'

def add_berries(request, pk):
    form = BerriesForm(request.POST)
    if form.is_valid():
        new_berries = form.save(commit=False)
        new_berries.pokemon_id = pk
        new_berries.save()
    return redirect('pokemons_detail', pk=pk)
