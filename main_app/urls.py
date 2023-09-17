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
    path('pokemons/<int:pk>/add_berries/', views.add_berries, name='add_berries'),
    path('pokemons/<int:pokemon_id>/assoc_item/<int:item_id>/', views.assoc_item, name='assoc_item'),
    path('pokemons/<int:pokemon_id>/unassoc_item/<int:item_id>/', views.unassoc_item, name='unassoc_item'),
    path('items/', views.ItemList.as_view(), name='items_index'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name ='items_detail'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
 ]