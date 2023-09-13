from django.urls import path
from .views import PokemonList, PokemonDetail
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemons/', PokemonList.as_view(), name='pokemons_index'),
    path('pokemons/<int:pk>/', PokemonDetail.as_view(), name='pokemons_detail'),
    path('pokemons/create/', views.PokemonCreate.as_view(), name='pokemons_create'),
    path('pokemons/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemons_update'),
    path('pokemons/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemons_delete'),
 ]