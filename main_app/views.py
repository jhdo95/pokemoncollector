from django.shortcuts import render

pokemons = [
    {'name': 'pikachu', 'type': 'electric', 'description': 'yellow electric mouse' },
    {'name': 'bulbasaur', 'type': 'grass', 'description': 'frog with flower back' },
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def pokemons_index(request):
    return render(request, 'pokemons/index.html', {
        'pokemons': pokemons
    })
