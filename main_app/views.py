from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item, Berries
from .forms import BerriesForm, ItemForm


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
         # Add the BerriesForm to the context
        context['berries_form'] = BerriesForm()
        # Query for berries associated with this pokemon
        context['pokemon_berries'] = Berries.objects.filter(pokemon=self.object)
        # Query for items associated with this pokemon (assuming a ForeignKey from Items to Pokemon)
        context['pokemon_items'] = Item.objects.filter(pokemon=self.object)
         # Query for unassociated items (items that are not associated with this pokemon)
        unassociated_items = Item.objects.exclude(pokemon=self.object)
        context['unassociated_items'] = unassociated_items
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

class ItemList(ListView):
    model = Item
    
class ItemDetail(DetailView):
    model = Item
    
class ItemCreate(CreateView):
    model = Item
    fields = '__all__'

class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'description']

class ItemDelete(DeleteView):
    model = Item
    success_url = '/items'

def add_item_to_pokemon(request, pokemon_id, item_id):
    # Retrieve the Pokemon and Item objects using the IDs
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    item = get_object_or_404(Item, pk=item_id)

    # Add the item to the Pokemon's items
    pokemon.items.add(item)

    # Redirect to the Pokemon detail page
    return redirect('pokemons_detail', pk=pokemon_id)


def assoc_item(request, pokemon_id, item_id):
  Pokemon.objects.get(id=pokemon_id).items.add(item_id)
  return redirect('pokemons_detail', pk=pokemon_id)


def unassoc_item(request, pokemon_id, item_id):
  Pokemon.objects.get(id=pokemon_id).items.remove(item_id)
  return redirect('pokemons_detail', pk=pokemon_id)

